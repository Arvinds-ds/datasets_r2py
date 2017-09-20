from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.dimes import dimes

def test_dimes():
  """Test module dimes.py by downloading dimes.csv and testing shape of 
    extracted data has 30 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = dimes(test_path)
  try:
    assert x_train.shape == (30,2)
  except:
    shutil.rmtree(test_path)
    raise()
 