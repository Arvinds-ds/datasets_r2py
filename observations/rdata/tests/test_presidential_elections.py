from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.presidential_elections import presidential_elections

def test_presidential_elections():
  """Test module presidential_elections.py by downloading presidential_elections.csv and testing shape of 
    extracted data has 1047 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = presidential_elections(test_path)
  try:
    assert x_train.shape == (1047,4)
  except:
    shutil.rmtree(test_path)
    raise()
 