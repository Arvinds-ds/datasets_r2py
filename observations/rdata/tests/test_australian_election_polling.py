from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.australian_election_polling import australian_election_polling

def test_australian_election_polling():
  """Test module australian_election_polling.py by downloading australian_election_polling.csv and testing shape of 
    extracted data has 239 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = australian_election_polling(test_path)
  try:
    assert x_train.shape == (239,14)
  except:
    shutil.rmtree(test_path)
    raise()
 