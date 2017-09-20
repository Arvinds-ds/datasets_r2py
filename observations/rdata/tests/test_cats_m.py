from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.cats_m import cats_m

def test_cats_m():
  """Test module cats_m.py by downloading cats_m.csv and testing shape of 
    extracted data has 97 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cats_m(test_path)
  try:
    assert x_train.shape == (97,3)
  except:
    shutil.rmtree(test_path)
    raise()
 