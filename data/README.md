# Data

This directory contains the data for both analyses of function-level and contract-level semantic properties.

## Data Sources

Both datasets have been sampled from the [skelcodes](https://github.com/gsalzer/skelcodes) dataset.

To obtain the skelcodes dataset the following steps are executed:

1. Cloning of the skelcode repository 
```bash
git clone https://github.com/gsalzer/skelcodes
```

2. Checkout of the commit `6881bb3`
```bash
git checkout 6881bb3
```

3. Removal of contracts without sources

To do this run the script `remove_contracts_without_source.py`, e.g. 

Note: This script has to be run from the skelcodes repository
```bash
python remove_contracts_without_source.py
```

### Function-level properties

The dataset for the function level properties consists of sampling 30 contracts randomly from 
the skelcodes contracts for which sources are available.
Also, as the evaluation script currently only supports annotations from a single file,
the contracts are further reduced to those where the source is present in a single file.

To do this run script `sample_30_for_function_properties.py`, e.g.
```bash
python sample_30_for_function_properties.py <skelcodes_directory> <output_directory>
```

This sample of 30 contracts was then annotated with the properties manually. For a list of all properties see the thesis.
Some limitations in the evaluation script (e.g. function definitions spanning multiple lines) have been avoided by altering the source code
in the corresponding ways where necessary.

### Contract level property token

The dataset for the function level properties consists of sampling 40 contracts randomly from 
the skelcodes contracts for which sources are available.
To get an even distribution of token and non-token contracts, we used the heuristic of checking if the 
ABI contains a function called "transfer", and sampled 20 from contracts containing a transfer, 
and 20 of the others.

The sampling is contained in `sample_40_for_token_property.py`, e.g.
```bash
python sample_40_for_token_property.py <skelcodes_directory> <output_directory>
```

The corresponding info.csv was exported as well, and the "is_token" column manually annotated.