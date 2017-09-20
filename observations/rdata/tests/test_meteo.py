from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.meteo import meteo

def test_meteo():
  """Test module meteo.py by downloading meteo.csv and testing shape of 
    extracted data has 11 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = meteo(test_path)
  try:
    assert x_train.shape == (11,6)
  except:
    shutil.rmtree(test_path)
    raise()
 