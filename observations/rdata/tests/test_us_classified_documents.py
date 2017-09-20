from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.us_classified_documents import us_classified_documents

def test_us_classified_documents():
  """Test module us_classified_documents.py by downloading us_classified_documents.csv and testing shape of 
    extracted data has 29 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_classified_documents(test_path)
  try:
    assert x_train.shape == (29,5)
  except:
    shutil.rmtree(test_path)
    raise()
 