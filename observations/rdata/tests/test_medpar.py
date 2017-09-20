from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.rdata.medpar import medpar

def test_medpar():
  """Test module medpar.py by downloading medpar.csv and testing shape of 
    extracted data has 1495 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = medpar(test_path)
  try:
    assert x_train.shape == (1495,10)
  except:
    shutil.rmtree(test_path)
    raise()
 