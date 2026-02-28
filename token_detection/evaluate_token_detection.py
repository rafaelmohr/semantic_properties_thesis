import pandas as pd
from tqdm import tqdm
import os
import subprocess
import sys
import json
import time
import re
from shutil import which
import argparse


assert which("gigahorse") is not None, "gigahorse not available in path"

parser = argparse.ArgumentParser()
parser.add_argument('input_dir')
args = parser.parse_args()
input_dir = args.input_dir

print(f"Input dir: {input_dir}")

contracts_df = pd.read_csv(f"{input_dir}/info.csv")

true_positive = []
false_positive = []
true_negative = []
false_negative = []

error = []

t_before = time.time()
execution_time_re = re.compile(
    r"completed in (\d+\.\d{2}) \+ (\d+\.\d{2}) \+ (\d+\.\d{2}) \+ (\d+\.\d{2}) secs",
    re.MULTILINE
    )

gigahorse_times, client_times = [], []


for index, row in tqdm(contracts_df.iterrows(), total=contracts_df.shape[0]):
    contract_id = row["contract_id"]

    contract_dir = f"{input_dir}/{contract_id}"

    hex_file = f"{contract_dir}/{row['filename']}"

    if not os.path.exists(hex_file):
        print(f"Hex file {hex_file} does not exist! Skipping..")
        continue

    gigahorse_command = [
        "gigahorse",
        "--restart",
        "-C", "/home/shared/gigahorse_clients/token_detection.dl,/home/gigahorse/clients/visualizeout.py",
        "--results_file", f"{contract_dir}/gigahorse-output/results.json",
        "--working_dir", f"{contract_dir}/gigahorse-output",
        f"{hex_file}"
    ]
    # gigahorse_command = f"gigahorse --rerun_clients -C /home/shared/clients/find_getter_functions.dl -w {contract_dir_abs_path}/gigahorse-output {hex_abs_path}"
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


    gigahorse_out_dir = f"{contract_dir}/gigahorse-output/{contract_id}/out"

    contract_is_token = row['is_token']

    tokencontract_file = f"{gigahorse_out_dir}/TokenContract.csv"

    try:
        with open(tokencontract_file, "rb") as f:
            line_count = sum(1 for _ in f)

        if line_count == 0:
            if contract_is_token: false_negative.append(contract_id)
            else: true_negative.append(contract_id)

        if line_count > 0:
            if contract_is_token: true_positive.append(contract_id)
            else: false_positive.append(contract_id)
    except Exception:
        error.append(contract_id)


elapsed = time.time() - t_before

print(f"True Positive:  {len(true_positive)}")
print(f"False Positive: {len(false_positive)}")
print(f"True Negative: {len(true_negative)}")
print(f"False Negative: {len(false_negative)}")
print(f"error: {len(error)}")

analysis_results = {
    "input_dir": input_dir,
    "time_elapsed_seconds": elapsed,
    "avg_time_per_contract_in_seconds": elapsed / contracts_df.shape[0],
    "avg_gigahorse_time_per_contract_in_seconds": sum(gigahorse_times) / len(gigahorse_times),
    "avg_client_time_per_contract_in_seconds": sum(client_times) / len(client_times),
    "true_positives": true_positive,
    "false_positive": false_positive,
    "true_negative": true_negative,
    "false_negative": false_negative,
    "error": error
}

with open(f"{input_dir}/analysis_results.json", "w") as f:
    json.dump(analysis_results, f, indent=4)