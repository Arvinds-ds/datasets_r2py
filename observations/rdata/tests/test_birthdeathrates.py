from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.birthdeathrates import birthdeathrates

def test_birthdeathrates():
  """Test module birthdeathrates.py by downloading birthdeathrates.csv and testing shape of 
    extracted data has 69 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = birthdeathrates(test_path)
  try:
    assert x_train.shape == (69,2)
  except:
    shutil.rmtree(test_path)
    raise()
 