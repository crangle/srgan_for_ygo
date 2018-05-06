# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import numpy as np
from glob import glob

if sys.version_info < (3, 0):
    from scipy import misc
else:
    import scipy.misc as misc

if __name__ == '__main__':
    hr_path = '../datasets/image_544x544/'
    lr_path = '../datasets/image_136x136/'
    f_list = glob(os.path.join(hr_path, '*.jpg')) + glob(os.path.join(hr_path, '*.png'))

    for f in f_list:
        im = misc.imread(f, mode='RGB')
        w, h, _ = im.shape
        im = misc.imresize(im, (w//4, h//4))
        save_path = os.path.join(lr_path, os.path.basename(f).split('.')[0]+'.tif')
        misc.imsave(save_path, im)
