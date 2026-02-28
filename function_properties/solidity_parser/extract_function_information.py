from typing import List

from solidity_parser.regex import mapping_re, array_re, prop_re, basic_type_of_array_re, int_type_size_re
from helpers import get_function_identifier, FunctionInfo, get_function_signature, normalize_arg_type


# for info on how getters are generated see:
# https://docs.soliditylang.org/en/latest/contracts.html#getter-functions

def handle_public_variable_definitions(definitions) -> List[FunctionInfo]:
    results: List[FunctionInfo] = []

    for var_def in definitions:

        function_arg = ""

        type_info = var_def["type_info"]

        name = var_def["name"]

        # check if mapping, array or just "scalar"
        mapping_match = mapping_re.search(type_info)
        array_match = array_re.search(type_info)

        if mapping_match:
            key_type = mapping_match.group(1).strip()

            function_arg = key_type

        elif array_match:
            # function arg for array getter is always uint256
            function_arg = "uint256"

        function_sig = f"{name}({function_arg})"
        function_id = get_function_identifier(function_sig)

        f_info = FunctionInfo(
            func_sig=function_sig,
            func_id=function_id,
            properties=[]
        )

        for line in var_def["comment_lines"]:
            matches = [m.group(1) for m in prop_re.finditer(line)]
            f_info.properties += matches

        results.append(f_info)

    return results


def handle_function_definition(functions_with_comments) -> List[FunctionInfo]:
    results: List[FunctionInfo] = []

    for item in functions_with_comments:

        f_info = FunctionInfo(
            func_sig=get_function_signature(item["def"]),
            func_id=get_function_identifier(get_function_signature(item["def"])),
            properties=[]
        )

        for line in item["comment_lines"]:
            matches = [m.group(1) for m in prop_re.finditer(line)]
            f_info.properties += matches

        results.append(f_info)

    return results


def is_data_type(type_info: str):
    data_types_starts = (
        "string",
        "uint",
        "int",
        "bytes",
        "bool",
        "address",
        "mapping",
        "bytes"
    )

    if type_info.startswith(data_types_starts): return True

    return False


def get_type_size(type: str) -> int:
    if type == "address" or type == "payable" or type == "address payable": return 20
    if type == "bool": return 1

    m = int_type_size_re.match(normalize_arg_type(type))
    if not m:
        raise Exception(f"Unrecognized type {type}")

    size_in_bytes = int(int(m.group(1)) / 8)
    return size_in_bytes
