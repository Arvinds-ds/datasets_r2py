from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.cubits import cubits

def test_cubits():
  """Test module cubits.py by downloading cubits.csv and testing shape of 
    extracted data has 9 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cubits(test_path)
  try:
    assert x_train.shape == (9,8)
  except:
    shutil.rmtree(test_path)
    raise()
 