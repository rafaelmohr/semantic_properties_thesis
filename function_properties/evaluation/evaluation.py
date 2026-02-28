from dataclasses import dataclass, asdict
from typing import List
import os
import json


class FuncEvaluationResult:
    def __init__(self, func_sig: str, func_id: str,
                 expected_props: List[str], actual_props: List[str]):
        self.func_sig = func_sig
        self.func_id = func_id
        self.expected_props = expected_props
        self.actual_props = actual_props

    # return confusion matrix in form of (true_pos, false_pos, false_neg)
    def get_confusion_matrix(self) -> tuple[int, int, int]:
        # convert to sets to use set operations for finding union and difference
        expected_set = set(self.expected_props)
        actual_set = set(self.actual_props)

        correct = expected_set & actual_set
        missing = expected_set - actual_set
        unexpected = actual_set - expected_set
        return len(correct), len(missing), len(unexpected)


class ContractEvaluationResult:
    def __init__(self, name: str, contract_dir: str, results: List[FuncEvaluationResult]):
        self.name = name
        self.contract_dir = contract_dir
        self.func_results = results

    def add_function_result(self, result: FuncEvaluationResult):
        self.func_results.append(result)

    def write_to_file(self):
        out_path = os.path.join(self.contract_dir, f"{self.name}_results.json")
        with open(out_path, "w") as f:

            serializable_results = [r.__dict__ for r in self.func_results]

            json.dump(serializable_results, f, indent=4)

    # return confusion matrix in form of (true_pos, false_pos, false_neg)
    def get_confusion_matrix(self) -> tuple[int, int, int]:
        tp = sum(r.get_confusion_matrix()[0] for r in self.func_results)
        fp = sum(r.get_confusion_matrix()[1] for r in self.func_results)
        fn = sum(r.get_confusion_matrix()[2] for r in self.func_results)

        return tp, fp, fn

def calculate_overall_scores(results: List[ContractEvaluationResult]) -> dict:

    confusion_matrices = [r.get_confusion_matrix() for r in results]

    overall_tp = sum([m[0] for m in confusion_matrices])
    overall_fp = sum([m[2] for m in confusion_matrices])
    overall_fn = sum([m[1] for m in confusion_matrices])

    precision = calc_precision(overall_tp, overall_fp)
    recall = calc_recall(overall_tp, overall_fn)

    f1 = calc_f1(overall_tp, overall_fp, overall_fn)

    return {
        "true_positives": overall_tp,
        "false_positives": overall_fp,
        "false_negatives": overall_fn,
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }



def calculate_scores_per_property(results: List[ContractEvaluationResult]) -> dict:
    prop_stats = {}

    for contract in results:
        for func in contract.func_results:
            expected = set(func.expected_props)
            actual = set(func.actual_props)

            all_props = expected | actual

            for prop in all_props:
                if prop not in prop_stats:
                    prop_stats[prop] = {"tp": 0, "fp": 0, "fn": 0, "fp_values": [], "fn_values": []}

                if prop in expected and prop in actual:
                    prop_stats[prop]["tp"] += 1
                elif prop in actual and prop not in expected:
                    prop_stats[prop]["fp"] += 1
                    prop_stats[prop]["fp_values"].append(f"{contract.name}.{func.func_id}")
                elif prop in expected and prop not in actual:
                    prop_stats[prop]["fn"] += 1
                    prop_stats[prop]["fn_values"].append(f"{contract.name}.{func.func_sig}")

    # calcualte metrics for each property
    property_metrics = {}
    for prop, counts in prop_stats.items():
        tp = counts["tp"]
        fp = counts["fp"]
        fn = counts["fn"]

        fp_values = counts["fp_values"]
        fn_values = counts["fn_values"]

        precision = calc_precision(tp, fp)
        recall = calc_recall(tp, fn)
        f1 = calc_f1(tp, fp, fn)

        property_metrics[prop] = {
            "true_positives": tp,
            "false_positives": fp,
            "false_negatives": fn,
            "precision": round(precision, 4) if precision is not None else None,
            "recall": round(recall, 4) if recall is not None else None,
            "f1_score": round(f1, 4) if f1 is not None else None,
            "fp_values": fp_values,
            "fn_values": fn_values
        }

    return property_metrics


def calc_precision(tp: int, fp: int):
    return tp / (tp + fp) if (tp + fp) > 0 else None

def calc_recall(tp: int, fn: int):
    return tp / (tp + fn) if (tp + fn) > 0 else None

def calc_f1(tp: int, fp: int, fn: int):
    precision = calc_precision(tp, fp)
    recall = calc_recall(tp, fn)

    if precision is None: precision = 0
    if recall is None: recall = 0

    return (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else None