import argparse
from typing import List

from solidity_parser.regex import pub_var_re, prop_re, func_re, comment_line_re
from helpers import get_function_signature, get_function_identifier, FunctionInfo
from solidity_parser.extract_function_information import handle_public_variable_definitions, handle_function_definition


def parse_sol_file(path: str) -> List[FunctionInfo]:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    functions_with_comments = []
    pub_var_definitions_with_comments = []

    for line_number, line in enumerate(lines, 1):
        # search for function definitions
        function_match = func_re.search(line)

        pub_var_match = pub_var_re.search(line)

        if function_match or pub_var_match:
            comment_lines = []

            # walk back up and add all comment lines immediately above function definition
            # comment blocks /* */ are ignored here
            i = line_number - 1
            while i > 1:
                prev_line = lines[i - 1]

                # only append comment lines which start with // and recognizer prefix
                if comment_line_re.search(prev_line):
                    comment_lines.append(prev_line.strip())
                    i -= 1
                else: break

            if function_match:
                functions_with_comments.append({
                    "def": line,
                    "comment_lines": comment_lines
                })

            else:

                type_info = pub_var_match.group(1)
                name = pub_var_match.group(10)
                if name is None: name = pub_var_match.group(13)
                if name is None: raise RuntimeError("Name for public function definition not found")

                pub_var_definitions_with_comments.append({
                    "type_info": type_info,
                    "name": name,
                    "comment_lines": comment_lines
                })


    # build list of all function definitions with the extracted properties
    results: List[FunctionInfo] = [
        *handle_function_definition(functions_with_comments),
        *handle_public_variable_definitions(pub_var_definitions_with_comments)
    ]

    # due to inheritance we might have multiple definitions of the same function
    # to solve this we combine property lists of duplicates
    deduplicated_results = {}

    for func in results:
        func_id = func.func_id
        # if dict with current key exists it means we have already processed this function definition and can skip it
        if func_id in deduplicated_results: continue

        # find duplicates of current function
        duplicate_functions = [f for f in results if f.func_id == func_id]

        # combine all properties of functions which appear multiple times
        all_props = [prop for func_data in duplicate_functions for prop in func_data.properties]
        # drop duplicates
        all_props = list(set(all_props))

        if func.func_id == "0x24a3b013":
            print("we have it!!!!!!!!!!!!!!!")
            print("function sig")

        deduplicated_results[func_id] = FunctionInfo(
            func_sig=func.func_sig,
            func_id=func.func_id,
            properties=all_props
        )

    return list(deduplicated_results.values())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="path to solditiy input file")

    args = parser.parse_args()

    print(parse_sol_file(args.path))