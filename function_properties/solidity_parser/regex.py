import re

RECOGNIZER_PREFIX = "SEM-ANALYZER"

RECOGNIZER_CHAR = "#"
prop_re = re.compile(rf"{RECOGNIZER_CHAR}(\w+)")

comment_line_re = re.compile(rf"\s?\/\/\s?{RECOGNIZER_PREFIX}\s(#\w+)")


# regex for valid solidity identifier
# see https://docs.soliditylang.org/en/latest/grammar.html#syntax-rule-SolidityLexer.Identifier
ID = r"[a-zA-Z$_][a-zA-Z0-9$_]*"
TYPE_NAME = r"\w+\d{0,3} *(\[([1-9]{0,3})?\])?( payable)?"
DATA_LOC = r"memory|storage|calldata"
F_ARG = rf"({TYPE_NAME})( {DATA_LOC})? {ID}"
func_arg_re = re.compile(F_ARG)
ARG_LIST = rf"(?:{F_ARG}(?:,\s*{F_ARG})*)?"


# https://docs.soliditylang.org/en/latest/grammar.html#syntax-rule-SolidityParser.functionDefinition
# https://docs.soliditylang.org/en/latest/grammar.html#syntax-rule-SolidityParser.parameterList
FUNCTION_REGEX = rf"function *({ID}) *\(({ARG_LIST})\)"
func_re = re.compile(FUNCTION_REGEX)


# to detect public state variable definitions, except those which are marked constant
pub_var_re = re.compile(rf"(?:(({TYPE_NAME})|(mapping *\({TYPE_NAME} *=> *{TYPE_NAME}\)))) *public *(?!\s*constant)(?!immutable *)({ID})")

# to check if public variable definition is mapping
mapping_re = re.compile(rf"mapping *\(({TYPE_NAME}) *=> *({TYPE_NAME})\)")
# to check if public variable definition is array
array_re = re.compile(r"\w+\d{0,3} *(\[([1-9]{0,3})\])")

basic_type_of_array_re = re.compile(r"(\w*\d{0,3})\[\d*\]")

int_type_size_re = re.compile(r"(?:uint|int)(\d{1,3})")
