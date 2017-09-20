from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.socsupport import socsupport

def test_socsupport():
  """Test module socsupport.py by downloading socsupport.csv and testing shape of 
    extracted data has 95 rows and 20 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = socsupport(test_path)
  try:
    assert x_train.shape == (95,20)
  except:
    shutil.rmtree(test_path)
    raise()
 