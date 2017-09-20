from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.rdata.primates import primates

def test_primates():
  """Test module primates.py by downloading primates.csv and testing shape of 
    extracted data has 5 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = primates(test_path)
  try:
    assert x_train.shape == (5,2)
  except:
    shutil.rmtree(test_path)
    raise()
 