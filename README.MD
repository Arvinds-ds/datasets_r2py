Website: https://vincentarelbundock.github.io/Rdatasets/

dataset_r2py
=============

``dataset_r2py`` is a automated script to generate `observations` (edwardlib/observations) ready dataset source python files and corresponding test files for a collection of 1100+ datasets that were originally distributed alongside the statistical software environment ``R`` and some of its add-on packages.  The R datasets were originally collated by https://vincentarelbundock.github.io/Rdatasets/

Usage
=====

`$ python gen_data_files`

The starting point for the script is the `datasets_mod.csv` file that has the name, URL, documentation RST file, rows and colums etc. The script
used jinja template engines to convert `template.py`, `test_template.py` and `init_template.py` to generate templated python source code and test script in a format required by `observations` module

The source code is generated in `observations/rdata` folder and tests are generated in `observations/rdata/tests` folder

Motivation
=======

I wrote this script out of frustration in getting datasets in to python that were easily available in R esp when using Stan/Edward. Edward's observations is a promising module.


