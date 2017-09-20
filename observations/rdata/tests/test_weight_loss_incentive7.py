from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.weight_loss_incentive7 import weight_loss_incentive7

def test_weight_loss_incentive7():
  """Test module weight_loss_incentive7.py by downloading weight_loss_incentive7.csv and testing shape of 
    extracted data has 33 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = weight_loss_incentive7(test_path)
  try:
    assert x_train.shape == (33,2)
  except:
    shutil.rmtree(test_path)
    raise()
 