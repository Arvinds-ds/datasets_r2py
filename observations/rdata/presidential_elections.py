from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def presidential_elections(path):
  """elections for U.S. President, 1932-2012, by state

  Democratic share of the presidential vote, 1932-2012, in each state and
  the District of Columbia.

  -  statecharacter, name of state

  -  demVotenumeric, percent of the vote for president won by the
     Democratic candidate

  -  yearnumeric, integer

  -  southlogical, `TRUE` if state is one of the 11 states of the former
     Confederacy

  Note
  ~~~~

  1,047 observations, unbalanced panel data in long format. Hawaii and
  Alaska contribute data from 1960 onwards the District of Columbia
  contributes data from 1964 onward; Alabama has missing data for 1948 and
  1964.

  David Leip's Atlas of U.S. Presidential Elections
  http://uselectionsatlas.org

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `presidential_elections.csv`.
  Returns:

    Tuple of np.ndarray `x_train` with 1047 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = "presidential_elections.csv"
  if not os.path.exists(os.path.join(path, filename)):
    url = "https://raw.github.com/vincentarelbundock/Rdatasets/master/csv" \
          "/pscl/presidentialElections.csv"
    maybe_download_and_extract(path, url,
                               save_file_name="presidential_elections.csv",
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
