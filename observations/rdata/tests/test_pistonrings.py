from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.pistonrings import pistonrings

def test_pistonrings():
  """Test module pistonrings.py by downloading pistonrings.csv and testing shape of 
    extracted data has 4 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pistonrings(test_path)
  try:
    assert x_train.shape == (4,3)
  except:
    shutil.rmtree(test_path)
    raise()
 