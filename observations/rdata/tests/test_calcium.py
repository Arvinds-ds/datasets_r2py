from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.rdata.calcium import calcium

def test_calcium():
  """Test module calcium.py by downloading calcium.csv and testing shape of 
    extracted data has 27 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = calcium(test_path)
  try:
    assert x_train.shape == (27,2)
  except:
    shutil.rmtree(test_path)
    raise()
 