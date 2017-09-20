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


def free1(path):
  """Freedom of Speech Data
  
  Selection of individual-level survey data for freedom of speech.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `free1.csv`.
  Returns:
    Tuple of np.ndarray `x_train` with 450 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  path = os.path.expanduser(path)
  filename = "free1.csv"
  if not os.path.exists(os.path.join(path, filename)):
    url = "https://raw.github.com/vincentarelbundock/Rdatasets/master/csv/Zelig/free1.csv"
    maybe_download_and_extract(path, url,
			       save_file_name="free1.csv",
			       resume=False)

  data = pd.read_csv(os.path.join(path,filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata