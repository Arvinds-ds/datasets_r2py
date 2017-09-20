from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.immigration import immigration

def test_immigration():
  """Test module immigration.py by downloading immigration.csv and testing shape of 
    extracted data has 2485 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = immigration(test_path)
  try:
    assert x_train.shape == (2485,5)
  except:
    shutil.rmtree(test_path)
    raise()
 