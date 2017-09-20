from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.rdata.drivers import drivers

def test_drivers():
  """Test module drivers.py by downloading drivers.csv and testing shape of 
    extracted data has 192 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = drivers(test_path)
  try:
    assert x_train.shape == (192,2)
  except:
    shutil.rmtree(test_path)
    raise()
 