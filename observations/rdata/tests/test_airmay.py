from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.airmay import airmay

def test_airmay():
  """Test module airmay.py by downloading airmay.csv and testing shape of 
    extracted data has 31 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = airmay(test_path)
  try:
    assert x_train.shape == (31,4)
  except:
    shutil.rmtree(test_path)
    raise()
 