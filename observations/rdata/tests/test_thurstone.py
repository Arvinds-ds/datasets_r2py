from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.rdata.thurstone import thurstone

def test_thurstone():
  """Test module thurstone.py by downloading thurstone.csv and testing shape of 
    extracted data has 9 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = thurstone(test_path)
  try:
    assert x_train.shape == (9,9)
  except:
    shutil.rmtree(test_path)
    raise()
 