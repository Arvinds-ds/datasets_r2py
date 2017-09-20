from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import pandas as pd
import sys

sys.path.append('../../')
from observations.util import maybe_download_and_extract


def nidd_thresh(path):
  """The River Nidd Data
  
  These data represent high river levels of the River Nidd in Yorkshire
  above a threshold value of 65. These data are suitable for analysis with
  `gpd`.
  

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `nidd_thresh.csv`.
  Returns:
    Tuple of np.ndarray `x_train` with 154 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  path = os.path.expanduser(path)
  filename = "nidd_thresh.csv"
  if not os.path.exists(os.path.join(path, filename)):
    url = "https://raw.github.com/vincentarelbundock/Rdatasets/master/csv/evir/nidd.thresh.csv"
    maybe_download_and_extract(path, url,
			       save_file_name="nidd_thresh.csv",
			       resume=False)

  data = pd.read_csv(os.path.join(path,filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata