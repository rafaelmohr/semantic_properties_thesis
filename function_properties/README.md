# Evaluation script for function-level properties

The evaluation script for function-level properties is `e2e-analysis.py`.
It expects as input one positional argument, a directory which contains subdirectories of contracts.

Example:
```bash
python function_properties/e2e_evaluation.py data/sample_30_function_properties
```

The environment of this script needs Gigahorse to be available as an executable in PATH.
Depending on the environment, the paths of the Gigahorse clients need to be adapted (line 50 of `e2e-analysis.py`).
