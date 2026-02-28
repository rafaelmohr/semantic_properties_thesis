from typing import List

import yaml
import os
import csv

from helpers import FunctionInfo


def aggregate_results(contract_dir: str, contract_name: str)->List[FunctionInfo]:
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)

    relative_gigahorse_output_dir = config.get('relative_gigahorse_output_dir').replace(
        '<contract_name>', contract_name
    )
    results_dir = os.path.join(contract_dir, relative_gigahorse_output_dir)

    results_dict = {}

    for analysis in config.get('analyses', []):
        property_name = analysis.get('name')
        relation_name = analysis.get("relation_name")
        parametric = analysis.get("parametric")

        csv_path = os.path.join(results_dir, f'{relation_name}.csv')
        if not os.path.exists(csv_path): continue # no results found for this analysis


        with open(csv_path, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            rows = list(reader)

            for row in rows:

                # at this point use the internal function id as output by analysis (jumpdest of first function block)
                function_id_internal = row[0]

                if not function_id_internal in results_dict:
                    results_dict[function_id_internal] = []

                property_string = property_name
                if parametric:
                    parameter_value = row[1]
                    property_string += parameter_value

                results_dict[function_id_internal].append(property_string)


    # aggregate functions into list and convert to public function id (first 4 bytes of function sig hash)
    function_id_map = {}
    with open(os.path.join(results_dir, "PublicFunctionId.csv"), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in list(reader):
            internal_id = row[0]
            public_id = row[1]
            function_id_map[internal_id] = public_id

    functions_with_props = []
    for key, value in results_dict.items():

        # if key not in function_id_map -> private function, we don't care about those
        if not key in function_id_map: continue

        functions_with_props.append(FunctionInfo(
            func_sig = "",
            func_id = function_id_map[key],
            properties = value
        ))

    return functions_with_props