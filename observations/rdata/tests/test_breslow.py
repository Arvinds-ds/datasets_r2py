from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.rdata.breslow import breslow

def test_breslow():
  """Test module breslow.py by downloading breslow.csv and testing shape of 
    extracted data has 10 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = breslow(test_path)
  try:
    assert x_train.shape == (10,5)
  except:
    shutil.rmtree(test_path)
    raise()
 