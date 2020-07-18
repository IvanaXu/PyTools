#
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

data = fits.open("059.Test_watch_fits.fits")
data.verify('fix')
img_data = np.flipud(data[1].data)
print(img_data, img_data.shape)

plt.imshow(img_data, cmap='gray')
plt.colorbar()
plt.savefig("059.Test_watch_fits.png")
plt.show()

# [[59702. 60107. 61022. ... 58985. 58754. 59741.]
#  [62138. 62183. 61586. ... 60122. 59813. 59714.]
#  [63515. 62870. 60941. ... 61337. 60986. 61034.]
#  ...
#  [65117. 63881. 64103. ... 61094. 61136. 61403.]
#  [63815. 62948. 62831. ... 60512. 61328. 61130.]
#  [62774. 63392. 63326. ... 61307. 63275. 62309.]] (136, 291)