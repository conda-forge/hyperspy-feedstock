#!/bin/bash

rm -f pyproject.toml

$PYTHON -m pip install . --no-deps -vvv
