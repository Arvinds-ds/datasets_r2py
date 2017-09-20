from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.us_personal_expenditure import us_personal_expenditure

def test_us_personal_expenditure():
  """Test module us_personal_expenditure.py by downloading us_personal_expenditure.csv and testing shape of 
    extracted data has 5 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_personal_expenditure(test_path)
  try:
    assert x_train.shape == (5,5)
  except:
    shutil.rmtree(test_path)
    raise()
 