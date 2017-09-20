from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.mdvis import mdvis

def test_mdvis():
  """Test module mdvis.py by downloading mdvis.csv and testing shape of 
    extracted data has 2227 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mdvis(test_path)
  try:
    assert x_train.shape == (2227,13)
  except:
    shutil.rmtree(test_path)
    raise()
 