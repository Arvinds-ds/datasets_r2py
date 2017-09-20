#!/bin/sh
rm -rf observations/rdata
python gen_data_files.py
cd observations/rdata/tests
pytest *.py
