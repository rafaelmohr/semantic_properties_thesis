import os

runtime_dir = f"runtime"
source_dir = f"source"

delete_counter = 0

for tranche in os.listdir(runtime_dir):

    tranche_path = f"{runtime_dir}/{tranche}"

    if os.path.isdir(tranche_path):

        for file in os.listdir(tranche_path):

            if not file.endswith(".hex"): continue

            base_name = os.path.splitext(file)[0]

            potential_source_dir = f"{source_dir}/{tranche}/{base_name}"

            if not os.path.exists(potential_source_dir):
                os.remove(f"{tranche_path}/{file}")
                delete_counter += 1

print(f"Deleted {delete_counter} contracts without available source-code")
