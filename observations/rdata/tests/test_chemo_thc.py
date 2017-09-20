from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.chemo_thc import chemo_thc

def test_chemo_thc():
  """Test module chemo_thc.py by downloading chemo_thc.csv and testing shape of 
    extracted data has 2 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = chemo_thc(test_path)
  try:
    assert x_train.shape == (2,4)
  except:
    shutil.rmtree(test_path)
    raise()
 