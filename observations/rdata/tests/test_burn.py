from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.burn import burn

def test_burn():
  """Test module burn.py by downloading burn.csv and testing shape of 
    extracted data has 154 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = burn(test_path)
  try:
    assert x_train.shape == (154,18)
  except:
    shutil.rmtree(test_path)
    raise()
 