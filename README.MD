dataset_r2py
=============

``dataset_r2py`` is a automated script to generate `observations`  (edwardlib/observations) ready  python files and corresponding unit test files for a collection of 1100+ datasets (1100 python files) that were originally distributed alongside the statistical software environment ``R`` and some of its add-on packages. 

 The R datasets were originally collated by https://vincentarelbundock.github.io/Rdatasets/

Usage
=====

`$ python gen_data_files`

The starting point for the script is the `datasets_mod.csv` file that has the name, URL, documentation RST file, rows and colums etc. The script
used jinja template engines to convert `template.tpl`, `test_template.tpl` and `init_template.tpl` to generate templated python source code and test script in a format required by `observations` module. The rst file is used to generate the doc string in python source.

The source code is generated in `observations/rdata` folder and tests are generated in `observations/rdata/tests` folder

The test file `./test_script.sh` performs the end to end testing of generating python source and test files and runs pytest on test files to download/load and verify the data.data 

Motivation
=======

I wrote this script out of frustration in getting datasets in to python that were easily available in R esp when using Stan/Edward. Edward's observations is a promising module.


