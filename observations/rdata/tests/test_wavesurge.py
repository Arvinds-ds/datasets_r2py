from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

sys.path.append('../../../')
from observations.rdata.wavesurge import wavesurge

def test_wavesurge():
  """Test module wavesurge.py by downloading wavesurge.csv and testing shape of 
    extracted data has 2894 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wavesurge(test_path)
  try:
    assert x_train.shape == (2894,2)
  except:
    shutil.rmtree(test_path)
    raise()
 