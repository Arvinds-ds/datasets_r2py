from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.pressure import pressure

def test_pressure():
  """Test module pressure.py by downloading pressure.csv and testing shape of 
    extracted data has 19 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pressure(test_path)
  try:
    assert x_train.shape == (19,2)
  except:
    shutil.rmtree(test_path)
    raise()
 