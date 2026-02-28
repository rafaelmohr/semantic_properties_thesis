# Evaluation script for contract-level property Token Contract

The evaluation script for the contract-level property is `evaluate_token_detection.py`.
It expects as input a positional argument of a directory, which contains subdirectories of contracts,
and an `info.csv` file containing information about these contracts.

Example:
```bash
python token_detection/e2e_evaluation.py data/sample_40_for_token_property
```

The environment of this script needs Gigahorse to be available as an executable in PATH.
Depending on the environment, the paths of the Gigahorse clients might need to be adapted (line 54 of `evaluate_token_detection.py`).
