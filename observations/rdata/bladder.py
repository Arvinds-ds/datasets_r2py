from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bladder(path):
  """Bladder Cancer Recurrences

  Data on recurrences of bladder cancer, used by many people to
  demonstrate methodology for recurrent event modelling.

  Bladder1 is the full data set from the study. It contains all three
  treatment arms and all recurrences for 118 subjects; the maximum
  observed number of recurrences is 9.

  Bladder is the data set that appears most commonly in the literature. It
  uses only the 85 subjects with nonzero follow-up who were assigned to
  either thiotepa or placebo, and only the first four recurrences for any
  patient. The status variable is 1 for recurrence and 0 for everything
  else (including death for any reason). The data set is laid out in the
  competing risks format of the paper by Wei, Lin, and Weissfeld.

  Bladder2 uses the same subset of subjects as bladder, but formatted in
  the (start, stop] or Anderson-Gill style. Note that in transforming from
  the WLW to the AG style data set there is a quite common programming
  mistake that leads to extra follow-up time for 12 subjects: all those
  with follow-up beyond their 4th recurrence). Over this extended time
  these subjects are by definition not at risk for another event in the
  WLW data set.

  bladder1

  id:

  Patient id

  treatment:

  Placebo, pyridoxine (vitamin B6), or thiotepa

  number:

  Initial number of tumours (8=8 or more)

  size:

  Size (cm) of largest initial tumour

  recur:

  Number of recurrences

  start,stop:

  The start and end time of each time interval

  status:

  End of interval code, 0=censored, 1=recurrence,

  2=death from bladder disease, 3=death other/unknown cause

  rtumor:

  Number of tumors found at the time of a recurrence

  rsize:

  Size of largest tumor at a recurrence

  enum:

  Event number (observation number within patient)

  bladder

  id:

  Patient id

  rx:

  Treatment 1=placebo 2=thiotepa

  number:

  Initial number of tumours (8=8 or more)

  size:

  size (cm) of largest initial tumour

  stop:

  recurrence or censoring time

  enum:

  which recurrence (up to 4)

  bladder2

  id:

  Patient id

  rx:

  Treatment 1=placebo 2=thiotepa

  number:

  Initial number of tumours (8=8 or more)

  size:

  size (cm) of largest initial tumour

  start:

  start of interval (0 or previous recurrence time)

  stop:

  recurrence or censoring time

  enum:

  which recurrence (up to 4)

  Andrews DF, Hertzberg AM (1985), DATA: A Collection of Problems from
  Many Fields for the Student and Research Worker, New York:
  Springer-Verlag.

  LJ Wei, DY Lin, L Weissfeld (1989), Regression analysis of multivariate
  incomplete failure time data by modeling marginal distributions.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bladder.csv`.
  Returns:

    Tuple of np.ndarray `x_train` with 340 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bladder.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/survival/bladder.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bladder.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
