from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.weight_loss_incentive import weight_loss_incentive

def test_weight_loss_incentive():
  """Test module weight_loss_incentive.py by downloading weight_loss_incentive.csv and testing shape of 
    extracted data has 38 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = weight_loss_incentive(test_path)
  try:
    assert x_train.shape == (38,3)
  except:
    shutil.rmtree(test_path)
    raise()
 