from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.rdata.discoveries import discoveries

def test_discoveries():
  """Test module discoveries.py by downloading discoveries.csv and testing shape of 
    extracted data has 100 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = discoveries(test_path)
  try:
    assert x_train.shape == (100,2)
  except:
    shutil.rmtree(test_path)
    raise()
 