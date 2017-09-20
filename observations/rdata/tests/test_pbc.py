from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.pbc import pbc

def test_pbc():
  """Test module pbc.py by downloading pbc.csv and testing shape of 
    extracted data has 418 rows and 20 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pbc(test_path)
  try:
    assert x_train.shape == (418,20)
  except:
    shutil.rmtree(test_path)
    raise()
 