from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.federalist import federalist

def test_federalist():
  """Test module federalist.py by downloading federalist.csv and testing shape of 
    extracted data has 7 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = federalist(test_path)
  try:
    assert x_train.shape == (7,2)
  except:
    shutil.rmtree(test_path)
    raise()
 