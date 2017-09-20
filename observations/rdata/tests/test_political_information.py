from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.political_information import political_information

def test_political_information():
  """Test module political_information.py by downloading political_information.csv and testing shape of 
    extracted data has 1807 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = political_information(test_path)
  try:
    assert x_train.shape == (1807,8)
  except:
    shutil.rmtree(test_path)
    raise()
 