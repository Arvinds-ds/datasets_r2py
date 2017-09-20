from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.gasprice import gasprice

def test_gasprice():
  """Test module gasprice.py by downloading gasprice.csv and testing shape of 
    extracted data has 695 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gasprice(test_path)
  try:
    assert x_train.shape == (695,2)
  except:
    shutil.rmtree(test_path)
    raise()
 