# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import tensorlayer as tl

# from config import config, log_config
#
# img_path = config.TRAIN.img_path

import os
import scipy
import numpy as np


def load_csv_list(path):
    with open(path, 'r') as f:
        f_str = f.readlines()
    f_list = [l.split('\n')[0] for l in f_str[1:]]
    return f_list


def get_imgs_fn(file_name, path):
    """ Input an image path and name, return an image array """
    return scipy.misc.imread(os.path.join(path, file_name), mode='RGB')


def crop_sub_imgs_fn(x, is_random=True):
    x = tl.prepro.crop(x, wrg=384, hrg=384, is_random=is_random)
    x = x / (255. / 2.)
    x = x - 1.
    return x


def downsample_fn(x):
    # We obtained the LR images by downsampling the HR images using bicubic kernel with downsampling factor r = 4.
    x = tl.prepro.imresize(x, size=[96, 96], interp='bicubic', mode=None)
    x = x / (255. / 2.)
    x = x - 1.
    return x