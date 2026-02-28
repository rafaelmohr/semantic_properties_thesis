import os
import pandas as pd
import shutil
import argparse
from tqdm import tqdm


def exactly_one_sol_file(directory):
    if not os.path.isdir(str(directory)):
        return False

    # count files ending in .sol
    files = os.listdir(directory)
    sol_files = [f for f in files if f.endswith('.sol')]
    return len(sol_files) == 1


parser = argparse.ArgumentParser()
parser.add_argument("skelcodes_dir", type=str, help="Directory of skelcodes repository")
parser.add_argument("output_dir", type=str, help="Output dir for sampled contracts")

args = parser.parse_args()
skelcodes_dir = args.skelcodes_dir
output_dir = args.output_dir


sample_size = 30

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

# filter to contracts where source is present in a single solidity file, not multiple
only_with_source_in_one_file_df = only_with_source_info_df[only_with_source_info_df["source_path"].apply(exactly_one_sol_file)]


# sample randomly
sample = only_with_source_in_one_file_df.sample(n = sample_size, random_state = 123)

# make output dir
os.makedirs(output_dir, exist_ok=True)

# copy all sources and the .hex to the output directory
for index, row in tqdm(sample.iterrows(), total=sample.shape[0]):
    contract_id = row["contract_id"]
    tranche = row["subdir"]
    filename = row["filename"]

    source_path = f"{source_dir}/{tranche}/{contract_id}"
    if not os.path.exists(source_path):
        print("source path not found", source_path)

    contract_out_dir = f"{output_dir}/{contract_id}"

    shutil.copytree(source_path, contract_out_dir)

    shutil.copyfile(f"{runtime_dir}/{tranche}/{filename}", f"{contract_out_dir}/{filename}")

# export info of sample
sample.to_csv(f"{output_dir}/info.csv", index = False)

print(f"Done! Results exported to {output_dir}")