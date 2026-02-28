from dataclasses import dataclass

import sha3
from solidity_parser.regex import func_re, func_arg_re

@dataclass
class FunctionInfo:
    func_sig: str
    func_id: str
    properties: list

def get_function_identifier(func_sig: str)-> str:
    """
    compute the 4 byte function identifier as it is used by the compiler
    """

    k = sha3.keccak_256()
    k.update(func_sig.encode("ascii"))
    func_id = "0x" + k.hexdigest()[:8]

    return func_id


def get_function_signature(func_def: str)-> str:
    """
    get function signature from function definition
    this essentially means only keeping the name and the normalized argument types
    """
    match = func_re.search(func_def)

    func_name = match.group(1)
    if func_name is None: raise RuntimeError("function name could not be extracted!")

    arg_list = match.group(2)
    # get only (non-normalized) types from function arg list
    arg_types = [m.group(1) for m in func_arg_re.finditer(arg_list)]

    normalized_arg_types = [normalize_arg_type(t) for t in arg_types]

    return f"{func_name}({','.join(normalized_arg_types)})"


def normalize_arg_type(input: str) -> str:
    if input is None: raise RuntimeError("arg type is None")
    
    if input == "uint" or input == "int": return f"{input}256"

    # address payable only exists at compile-time
    if input == "address payable": return "address"

    return input