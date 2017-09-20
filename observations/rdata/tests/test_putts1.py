from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.putts1 import putts1

def test_putts1():
  """Test module putts1.py by downloading putts1.csv and testing shape of 
    extracted data has 587 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = putts1(test_path)
  try:
    assert x_train.shape == (587,2)
  except:
    shutil.rmtree(test_path)
    raise()
 