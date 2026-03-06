# Evaluation script for function-level properties

The evaluation script for function-level properties is `e2e-analysis.py`.
It expects as input one positional argument, a directory which contains subdirectories of contracts.

Example:
```bash
python function_properties/e2e_evaluation.py data/sample_30_function_properties
```

The environment of this script needs Gigahorse to be available as an executable in PATH.
Depending on the environment, the paths of the Gigahorse clients need to be adapted (line 50 of `e2e-analysis.py`).


## Note
The Solidity parsing component does not parse all public variable definitions correctly. 
Specifically, public variables which have another contract as type, and therefore appear as 
an address type in the bytecode, are incorrectly not extracted in the evaluation script.
As mentioned in section 5.2.3 of the thesis, these results were manually corrected there.

The best fix for this would be a comprehensive rewrite of the Solidity Parser.