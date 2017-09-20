from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.carrots import carrots

def test_carrots():
  """Test module carrots.py by downloading carrots.csv and testing shape of 
    extracted data has 24 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = carrots(test_path)
  try:
    assert x_train.shape == (24,4)
  except:
    shutil.rmtree(test_path)
    raise()
 