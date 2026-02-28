import os
import glob


# This script can be used to count number of overall annotated definitions and number of annotated properties

def analyze_sol_files(root_dir):
    overall_keyword_count = 0
    overall_property_count = 0


    # Get all items in the root directory
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)

        # Only process if it's a directory
        if os.path.isdir(item_path):
            # Find all .sol files in this subdirectory
            sol_files = glob.glob(os.path.join(item_path, "*.sol"))

            if len(sol_files) == 0:
                print(f"[ERROR] No .sol file found in: {item_path}")
                continue
            elif len(sol_files) > 1:
                print(f"[ERROR] Multiple .sol files found in: {item_path}")
                continue

            # Process the single .sol file
            sol_file = sol_files[0]
            keyword_count = 0
            property_count = 0

            try:
                with open(sol_file, 'r') as f:
                    for line in f:
                        clean_line = line.strip()
                        if clean_line.startswith("// SEM-ANALYZER"):
                            keyword_count += 1
                            # Count every occurrence of '#' in this specific line
                            property_count += clean_line.count('#')

            except Exception as e:
                print(f"[ERROR] Could not read file {sol_file}: {e}")

            overall_keyword_count += keyword_count
            overall_property_count += property_count

    print("Overall keyword SEM-ANALYZER found: ", overall_keyword_count)
    print("Overall properties found: ", overall_property_count)


if __name__ == "__main__":
    # Use '.' for the current directory or provide a specific path
    target_directory = "../data/sample_30_function_properties"
    analyze_sol_files(target_directory)