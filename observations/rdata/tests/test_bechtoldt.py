from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.bechtoldt import bechtoldt

def test_bechtoldt():
  """Test module bechtoldt.py by downloading bechtoldt.csv and testing shape of 
    extracted data has 17 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bechtoldt(test_path)
  try:
    assert x_train.shape == (17,17)
  except:
    shutil.rmtree(test_path)
    raise()
 