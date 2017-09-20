from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hbk(path):
  """Hawkins, Bradu, Kass's Artificial Data

  Artificial Data Set generated by Hawkins, Bradu, and Kass (1984). The
  data set consists of 75 observations in four dimensions (one response
  and three explanatory variables). It provides a good example of the
  masking effect. The first 14 observations are outliers, created in two
  groups: 1–10 and 11–14. Only observations 12, 13 and 14 appear as
  outliers when using classical methods, but can be easily unmasked using
  robust distances computed by, e.g., MCD - covMcd().

  A data frame with 75 observations on 4 variables, where the last
  variable is the dependent one.

  X1
      x[,1]

  X2
      x[,2]

  X3
      x[,3]

  Y
      y

  Note
  ~~~~

  This data set is also available in package wle as `artificial`.

  Hawkins, D.M., Bradu, D., and Kass, G.V. (1984) Location of several
  outliers in multiple regression data using elemental sets.
  *Technometrics* **26**, 197–208.

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection*; Wiley, p.94.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hbk.csv`.
  Returns:

    Tuple of np.ndarray `x_train` with 75 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = "hbk.csv"
  if not os.path.exists(os.path.join(path, filename)):
    url = "https://raw.github.com/vincentarelbundock/Rdatasets/master/csv" \
          "/robustbase/hbk.csv"
    maybe_download_and_extract(path, url,
                               save_file_name="hbk.csv",
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
