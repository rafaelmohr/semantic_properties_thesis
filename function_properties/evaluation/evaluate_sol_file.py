import argparse
import os
import csv

from helpers import FunctionInfo
from evaluation.evaluation import FuncEvaluationResult
from solidity_parser.solidity_parser import parse_sol_file
from analysis_aggregation.aggregate_results import aggregate_results

from evaluation.evaluation import ContractEvaluationResult


def evaluate_sol_file(contract_path: str, contract_name: str) -> ContractEvaluationResult:
    assert os.path.exists(contract_path), f"{contract_path} does not exist!"

    contract_dir, contract_file = os.path.split(contract_path)

    functions_with_props_expected = parse_sol_file(contract_path)
    functions_with_props_actual = aggregate_results(contract_dir, contract_name)

    with open(f"{contract_dir}/gigahorse-output/{contract_name}/out/PublicFunctionId.csv", 'r') as f:
        public_functions = [row[1] for row in csv.reader(f, delimiter="\t")]

    eval_result = ContractEvaluationResult(
        name=contract_name,
        contract_dir=contract_dir,
        results = []
    )

    for func_expected in functions_with_props_expected:

        if func_expected.func_id == "0x24a3b013":
            print("found it")
            print(func_expected.func_sig)
            print(func_expected.properties)

        func_actual_found = False
        func_actual = [f for f in functions_with_props_actual if f.func_id == func_expected.func_id]

        if len(func_actual) == 0:
            # function not being found in analysis data principally means that no properties have been found for it
            # in that case create empty property list to compare it with expected properties
            # but it might be that properties are defined in the source for a contract code which did not get compiled
            # in that case just skip the expected function
            if not func_expected.func_id in public_functions:
                continue

            func_actual = FunctionInfo(
                func_sig = "",
                func_id = func_expected.func_id,
                properties = []
            )
        else:
            func_actual = func_actual[0]
            func_actual_found = True

        eval_result.add_function_result(FuncEvaluationResult(
            func_expected.func_sig,
            func_expected.func_id,
            expected_props=func_expected.properties.copy(),
            actual_props=func_actual.properties.copy(),
        ))

        if func_actual_found: functions_with_props_actual.remove(func_actual)


    # if at this point there are functions left over, it means that our tool detected properties for a function for which it is not expected
    for func_actual in functions_with_props_actual:
        eval_result.add_function_result(FuncEvaluationResult(
            "",
            func_actual.func_id,
            [],
            func_actual.properties
        ))

    eval_result.write_to_file()

    return eval_result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("contract_path")

    args = parser.parse_args()

    evaluate_sol_file(args.contract_path)