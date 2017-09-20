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


def mendel_abc(path):
  """Mendel's F2 trifactorial data for seed shape (A: round or wrinkled), cotyledon color (B: albumen yellow or green), and seed coat color (C: grey-brown or white)
  
  The `mendel3` data frame has 27 rows and 4 columns. Data are from
  Mendel (1886), and are reproduced in Fisher (1936) and Weir (1996).
  
  This data frame contains the following columns:
  
  seedshape
      Factor with levels: `AA`, `Aa` and `aa`
  
  cotylcolor
      Factor with levels: `BB`, `Bb` and `bb`
  
  coatcolor
      Factor with levels: `CC`, `Cc` and `cc`
  
  Observed
      a numeric vector that holds the frequencies.
  
  Data are from Mendel (1886), and are reproduced in Fisher (1936) and
  Weir (1996).

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `mendel_abc.csv`.
  Returns:
    Tuple of np.ndarray `x_train` with 27 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  path = os.path.expanduser(path)
  filename = "mendel_abc.csv"
  if not os.path.exists(os.path.join(path, filename)):
    url = "https://raw.github.com/vincentarelbundock/Rdatasets/master/csv/hwde/mendelABC.csv"
    maybe_download_and_extract(path, url,
			       save_file_name="mendel_abc.csv",
			       resume=False)

  data = pd.read_csv(os.path.join(path,filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata