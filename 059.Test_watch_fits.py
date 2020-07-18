#
"""
格式介绍
FITS (Flexible Image Transport System)是天文学界常用的数据格式，它专门为在不同平台之间交换数据而设计。1988年的国际天文学联合会（IAU）大会指定IAU的FITS工作组全权负责此格式的修订。IAU规定，今后对FITS标准的修改不得破坏前后一致性，也就是所谓的“once FITS, always FITS”一说。

详细参数
FITS文件由文件头和数据组成。在文件头中存储有对该文件的描述，如观测时间、观测对象、拍照温度、曝光时间等信息，同时也可以在文件头中注明观测时的视场、精度等，便于后期数据分析之用。文件头部分每行占80个字符，并以END结尾。按南京大学郑兴武教授所编《现代天体物理实验指导》一书中的说法，文件头共有36行，若未满则以空格补之。但我发现实际上某些FITS文件的头部要长于此值。每行的数据值一般为右对齐，“/”之后是注释内容。其具体表示格式是：
Keyword = Value /Comments
其中Value部分可以为空。较重要的几项有：BITPIX（指明图象位数）、NAXIS（指明图象维数）、NAXISn（代表第n维的像素数）。数据部分可以是图象或其他信息（如数据表），这些数据按头部所给出的描述组织。
"""
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