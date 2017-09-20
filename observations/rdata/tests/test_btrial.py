from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.btrial import btrial

def test_btrial():
  """Test module btrial.py by downloading btrial.csv and testing shape of 
    extracted data has 45 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = btrial(test_path)
  try:
    assert x_train.shape == (45,3)
  except:
    shutil.rmtree(test_path)
    raise()
 