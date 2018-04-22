# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import scipy
import numpy as np
from glob import glob


if __name__ == '__main__':
    hr_path = '../datasets/image_544x544/'
    lr_path = '../datasets/image_136x136/'
    f_list = glob(os.path.join(hr_path, '*.jpg')) + glob(os.path.join(hr_path, '*.png'))

    for f in f_list:
        im = scipy.misc.imread(f, mode='RGB')
        w, h, _ = im.shape
        im = scipy.misc.imresize(im, (w//4, h//4))
        save_path = os.path.join(lr_path, os.path.basename(f))
        scipy.misc.imsave(save_path, im)
