#!/bin/sh
rm -rf observations/r
rm -rf tests/r
python gen_data_files.py
touch tests/__init__.py
touch tests/r/__init__.py
#cd observations/rdata/tests
#pytest *.py
