from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.ovarian import ovarian

def test_ovarian():
  """Test module ovarian.py by downloading ovarian.csv and testing shape of 
    extracted data has 26 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ovarian(test_path)
  try:
    assert x_train.shape == (26,6)
  except:
    shutil.rmtree(test_path)
    raise()
 