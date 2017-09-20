from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.melanoma import melanoma

def test_melanoma():
  """Test module melanoma.py by downloading melanoma.csv and testing shape of 
    extracted data has 37 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = melanoma(test_path)
  try:
    assert x_train.shape == (37,2)
  except:
    shutil.rmtree(test_path)
    raise()
 