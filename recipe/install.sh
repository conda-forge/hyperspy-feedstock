#!/bin/bash

rm -f pyproject.toml

$PYTHON -m pip install . --no-deps --use-feature=in-tree-build -vvv
