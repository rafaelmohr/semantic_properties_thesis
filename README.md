# Source for the master thesis "Semantic Properties in Ethereum Bytecode using Static Analysis"

This repository contains the accompanying files for the master thesis "Semantic Properties in Ethereum Bytecode using Static Analysis".

## Installation

If you run this on your own system (i.e. not in a docker container) I suggest
using a venv. 

Install dependencies via:
```bash
pip install -r requirements.txt
```

The docker image provides Python 3.10, with which all script were run, but older versions might also work.

## Structure

This project is structured as follows:

- data: this directory contains the data used in the evaluation, as well as the scripts and a description on how this data was collected.
- docker: contains a dockerfile to build an image where Gigahorse is correctly installed with its dependencies.
- gigahorse_clients: contains all Datalog clients
- function_properties: contains the files for the evaluation of the function level properties
- token_detection: contains the script for the evaluation of the token contract detection

Each directory contains its own README which explains how to run the scripts.