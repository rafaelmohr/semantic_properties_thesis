import os
import pandas as pd
import shutil
import argparse
from tqdm import tqdm
import json


def exactly_one_sol_file(directory):
    if not os.path.isdir(str(directory)):
        return False

    # count files ending in .sol
    files = os.listdir(directory)
    sol_files = [f for f in files if f.endswith('.sol')]
    return len(sol_files) == 1

def check_abi_contains_transfer(contract_source_path):
    abi_files = [f for f in os.listdir(contract_source_path) if f.endswith('.abi')]

    if not len(abi_files) == 1:
        return False

    abi_file_path = f"{contract_source_path}/{abi_files[0]}"

    if not os.path.exists(abi_file_path):
        return False

    with open(abi_file_path, "r") as f:
        abi = json.load(f)

        for abi_entry in abi:
            if abi_entry["type"] == "function" and abi_entry["name"] == "transfer":
                return True

    return False


parser = argparse.ArgumentParser()
parser.add_argument("skelcodes_dir", type=str, help="Directory of skelcodes repository")
parser.add_argument("output_dir", type=str, help="Output dir for sampled contracts")

args = parser.parse_args()
skelcodes_dir = args.skelcodes_dir
output_dir = args.output_dir


sample_size = 40
transfer_function_split = 1/2

print(f"Sampling {sample_size} contracts randomly...")

runtime_dir = f"{skelcodes_dir}/runtime"
source_dir = f"{skelcodes_dir}/source"

info_df = pd.read_csv(f"{skelcodes_dir}/info.csv")

# add subdirectory as column and build path
info_df["subdir"] = info_df["block"].astype(str).str[:-6] + 'xxxxxx'
info_df.loc[info_df["subdir"] == "xxxxxx", "subdir"] = "0xxxxxx"

info_df["contract_id"] = info_df["filename"].astype(str).str[:-4]

info_df["source_path"] = source_dir + "/" + info_df["subdir"] + "/" + info_df["contract_id"]

# filter to contracts for which source is present
only_with_source_info_df = info_df[info_df["source_path"].apply(os.path.exists)]

# divide dataframe into contracts containing a transfer function in ABI and not
transfer_exists_mask = only_with_source_info_df["source_path"].apply(check_abi_contains_transfer)
with_transfer_func_df = only_with_source_info_df[transfer_exists_mask]
no_transfer_func_df = only_with_source_info_df[~transfer_exists_mask]
with_transfer_sample_size = round(sample_size * transfer_function_split)
no_transfer_sample_size = sample_size - with_transfer_sample_size

with_transfer_sample_df = with_transfer_func_df.sample(n = with_transfer_sample_size, random_state = 123)
with_transfer_sample_df["abi_contains_transfer"] = True

no_transfer_sample_df = no_transfer_func_df.sample(n = no_transfer_sample_size, random_state = 123)
no_transfer_sample_df["abi_contains_transfer"] = False

# only keep relevant columns
final_sample = pd.concat([with_transfer_sample_df, no_transfer_sample_df])[["filename", "subdir", "contract_id", "source_path", "abi_contains_transfer"]]

# add column to later manually annotate if actually is a token contract or not
final_sample["is_token"] = False
# make output dir
os.makedirs(output_dir, exist_ok=True)

# copy all sources and the .hex to the output directory
for index, row in tqdm(final_sample.iterrows(), total=final_sample.shape[0]):
    contract_id = row["contract_id"]
    tranche = row["subdir"]
    filename = row["filename"]

    source_path = row["source_path"]
    if not os.path.exists(source_path):
        print("source path not found", source_path)

    contract_out_dir = f"{output_dir}/{contract_id}"

    shutil.copytree(source_path, contract_out_dir)

    shutil.copyfile(f"{runtime_dir}/{tranche}/{filename}", f"{contract_out_dir}/{filename}")

# export info of sample
final_sample.to_csv(f"{output_dir}/info.csv", index = False)

print(f"Done! Results exported to {output_dir}")