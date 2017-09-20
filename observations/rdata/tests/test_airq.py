from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.airq import airq

def test_airq():
  """Test module airq.py by downloading airq.csv and testing shape of 
    extracted data has 30 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = airq(test_path)
  try:
    assert x_train.shape == (30,6)
  except:
    shutil.rmtree(test_path)
    raise()
 