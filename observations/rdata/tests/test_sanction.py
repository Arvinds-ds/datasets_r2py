from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.sanction import sanction

def test_sanction():
  """Test module sanction.py by downloading sanction.csv and testing shape of 
    extracted data has 78 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sanction(test_path)
  try:
    assert x_train.shape == (78,8)
  except:
    shutil.rmtree(test_path)
    raise()
 