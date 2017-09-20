from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.rdata.cafe import cafe

def test_cafe():
  """Test module cafe.py by downloading cafe.csv and testing shape of 
    extracted data has 100 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cafe(test_path)
  try:
    assert x_train.shape == (100,7)
  except:
    shutil.rmtree(test_path)
    raise()
 