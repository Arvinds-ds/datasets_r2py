from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def melanoma(path):
  """Melanoma skin cancer incidence

  These data from the Connecticut Tumor Registry present age-adjusted
  numbers of melanoma skin-cancer incidences per 100,000 people in
  Connectict for the years from 1936 to 1972.

  A data frame with 37 observations on the following 2 variables.

  year
      Years 1936 to 1972.

  incidence
      Rate of melanoma cancer per 100,000 population.

  Note
  ~~~~

  This dataset is not related to the `melanoma` dataset in the **boot**
  package with the same name.

  The S-PLUS 6.2 help for the melanoma data says that the incidence rate
  is per *million*, but this is not consistent with data found at the
  National Cancer Institute (http://www.nci.nih.gov).

  Author(s)
  ~~~~~~~~~

  Documentation contributed by Kevin Wright.

  Houghton, A., E. W. Munster, and M. V. Viola. (1978). Increased
  Incidence of Malignant Melanoma After Peaks of Sunspot Activity. *The
  Lancet*, **8**, 759–760.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `melanoma.csv`.
  Returns:

    Tuple of np.ndarray `x_train` with 37 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = "melanoma.csv"
  if not os.path.exists(os.path.join(path, filename)):
    url = "https://raw.github.com/vincentarelbundock/Rdatasets/master/csv" \
          "/lattice/melanoma.csv"
    maybe_download_and_extract(path, url,
                               save_file_name="melanoma.csv",
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
