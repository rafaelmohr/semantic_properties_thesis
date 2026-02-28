import json
import os
import argparse
import time
from shutil import which
import subprocess
from tqdm import tqdm
import re

from evaluation.evaluate_sol_file import evaluate_sol_file
from evaluation.evaluation import calculate_overall_scores, calculate_scores_per_property


assert which("solc") is not None, "solc not available in path"
assert which("gigahorse") is not None, "gigahorse not available in path"

parser = argparse.ArgumentParser()
parser.add_argument('input_dir')
args = parser.parse_args()
input_dir = args.input_dir


contract_directories = [f"{input_dir}/{d}" for d in os.listdir(input_dir) if os.path.isdir(f"{input_dir}/{d}")]

print(f"Evaluating {len(contract_directories)} contracts..")
t_before = time.time()
execution_time_re = re.compile(
    r"completed in (\d+\.\d{2}) \+ (\d+\.\d{2}) \+ (\d+\.\d{2}) \+ (\d+\.\d{2}) secs",
    re.MULTILINE
)

gigahorse_times, client_times = [], []
results = []

for contract_dir in tqdm(contract_directories):

    contract_dir_abs_path = os.path.abspath(contract_dir)

    sol_files = [f for f in os.listdir(contract_dir) if (os.path.isfile(f"{contract_dir}/{f}") and f.endswith(".sol"))]
    assert len(sol_files) == 1, f"more than one or no solidity file found in {contract_dir}"
    sol_file_abs_path = f"{contract_dir_abs_path}/{sol_files[0]}"

    hex_files = [f for f in os.listdir(contract_dir) if (os.path.isfile(f"{contract_dir}/{f}") and f.endswith(".hex"))]
    assert len(hex_files) == 1, f"more than one or no hex file found in {contract_dir}"
    hex_abs_path = f"{contract_dir_abs_path}/{hex_files[0]}"

    contract_name = os.path.split(contract_dir_abs_path)[1]

    # run gigahorse with our client
    gigahorse_command = [
        "gigahorse",
        "--restart",
        "-C", "/home/shared/gigahorse_clients/function_properties/collection.dl,/home/gigahorse/clients/visualizeout.py",
        "--results_file", f"{contract_dir_abs_path}/gigahorse-output/results.json",
        "--working_dir", f"{contract_dir_abs_path}/gigahorse-output",
        f"{hex_abs_path}"
    ]
    try:
        result = subprocess.run(
            gigahorse_command,
            # shell=True,
            capture_output=True,
            text=True,
            check=True
        )

        # extract reported execution times from gigahorse output
        match = execution_time_re.search(result.stderr)
        if (match):
            gigahorse_time = float(match.group(1)) + float(match.group(2)) + float(match.group(3))
            client_time = float(match.group(4))
            gigahorse_times.append(gigahorse_time)
            client_times.append(client_time)

    except subprocess.CalledProcessError as e:
        print("GIGAHORSE ERROR")
        print(f"{e.stderr}")
        print(f"{e.stdout}")
        break


    # compare output of gigahorse to properties defined in source code
    results.append(evaluate_sol_file(sol_file_abs_path, contract_name))


elapsed = time.time() - t_before

# calculate scores both on overall level and per property
output = {
    "input_dir": input_dir,
    "time_elapsed": elapsed,
    "avg_time_per_contract_in_seconds": elapsed / len(contract_directories),
    "avg_gigahorse_time_per_contract_in_seconds": sum(gigahorse_times) / len(gigahorse_times),
    "avg_client_time_per_contract_in_seconds": sum(client_times) / len(client_times),
    "overall": calculate_overall_scores(results),
    "per_property": calculate_scores_per_property(results)
}

out_path = f"{input_dir}/evaluation_results.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=4)

print(f"Evaluation finished! Results written to {out_path}")
