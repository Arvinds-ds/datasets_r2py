from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.mgus import mgus

def test_mgus():
  """Test module mgus.py by downloading mgus.csv and testing shape of 
    extracted data has 241 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mgus(test_path)
  try:
    assert x_train.shape == (241,12)
  except:
    shutil.rmtree(test_path)
    raise()
 