from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.pluton import pluton

def test_pluton():
  """Test module pluton.py by downloading pluton.csv and testing shape of 
    extracted data has 45 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pluton(test_path)
  try:
    assert x_train.shape == (45,4)
  except:
    shutil.rmtree(test_path)
    raise()
 