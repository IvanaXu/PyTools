import sys
n = int(sys.argv[1])

@profile
def r():
  import pandas as pd
  import numpy as np
  import time
  N = n
  data = pd.DataFrame(np.random.uniform(1,9,(N, 38)))
  data[data[12] > 5]
  time.sleep(2)

r()