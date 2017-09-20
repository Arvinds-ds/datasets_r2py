from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.bids import bids

def test_bids():
  """Test module bids.py by downloading bids.csv and testing shape of 
    extracted data has 126 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bids(test_path)
  try:
    assert x_train.shape == (126,12)
  except:
    shutil.rmtree(test_path)
    raise()
 