from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.rdata.pair65 import pair65

def test_pair65():
  """Test module pair65.py by downloading pair65.csv and testing shape of 
    extracted data has 9 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pair65(test_path)
  try:
    assert x_train.shape == (9,2)
  except:
    shutil.rmtree(test_path)
    raise()
 