from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.bigcity import bigcity

def test_bigcity():
  """Test module bigcity.py by downloading bigcity.csv and testing shape of 
    extracted data has 49 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bigcity(test_path)
  try:
    assert x_train.shape == (49,2)
  except:
    shutil.rmtree(test_path)
    raise()
 