from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.weight_loss_incentive4 import weight_loss_incentive4

def test_weight_loss_incentive4():
  """Test module weight_loss_incentive4.py by downloading weight_loss_incentive4.csv and testing shape of 
    extracted data has 36 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = weight_loss_incentive4(test_path)
  try:
    assert x_train.shape == (36,2)
  except:
    shutil.rmtree(test_path)
    raise()
 