from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def psid3(path):
  """Labour Training Evaluation Data

  A non-experimental "control" group, used in various studies of the
  effect of a labor training program, alternative to the experimental
  control group in `nswdemo`.

  This data frame contains the following columns:

  trt
      a numeric vector identifying the study in which the subjects were
      enrolled (0 = Control, 1 = treated).

  age
      age (in years).

  educ
      years of education.

  black
      (0 = not black, 1 = black).

  hisp
      (0 = not hispanic, 1 = hispanic).

  marr
      (0 = not married, 1 = married).

  nodeg
      (0 = completed high school, 1 = dropout).

  re74
      real earnings in 1974.

  re75
      real earnings in 1975.

  re78
      real earnings in 1978.

  http://www.nber.org/~rdehejia/nswdata.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `psid3.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 128 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'psid3.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/DAAG/psid3.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='psid3.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata