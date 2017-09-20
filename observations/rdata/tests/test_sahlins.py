from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.sahlins import sahlins

def test_sahlins():
  """Test module sahlins.py by downloading sahlins.csv and testing shape of 
    extracted data has 20 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sahlins(test_path)
  try:
    assert x_train.shape == (20,2)
  except:
    shutil.rmtree(test_path)
    raise()
 