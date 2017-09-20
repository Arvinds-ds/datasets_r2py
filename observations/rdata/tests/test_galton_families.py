from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.galton_families import galton_families

def test_galton_families():
  """Test module galton_families.py by downloading galton_families.csv and testing shape of 
    extracted data has 934 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = galton_families(test_path)
  try:
    assert x_train.shape == (934,8)
  except:
    shutil.rmtree(test_path)
    raise()
 