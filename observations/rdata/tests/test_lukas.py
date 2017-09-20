from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.lukas import lukas

def test_lukas():
  """Test module lukas.py by downloading lukas.csv and testing shape of 
    extracted data has 85 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lukas(test_path)
  try:
    assert x_train.shape == (85,4)
  except:
    shutil.rmtree(test_path)
    raise()
 