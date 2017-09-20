from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.us_state_abbreviations import us_state_abbreviations

def test_us_state_abbreviations():
  """Test module us_state_abbreviations.py by downloading us_state_abbreviations.csv and testing shape of 
    extracted data has 76 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_state_abbreviations(test_path)
  try:
    assert x_train.shape == (76,10)
  except:
    shutil.rmtree(test_path)
    raise()
 