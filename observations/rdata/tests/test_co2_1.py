from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.rdata.co2_1 import co2_1

def test_co2_1():
  """Test module co2_1.py by downloading co2_1.csv and testing shape of 
    extracted data has 468 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = co2_1(test_path)
  try:
    assert x_train.shape == (468,2)
  except:
    shutil.rmtree(test_path)
    raise()
 