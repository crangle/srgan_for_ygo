# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from glob import glob
import random


def save_as_csv(path, f_list):
    with open(path, 'w') as f:
        f.write('path\n')
        for l in f_list:
            f.write('{}\n'.format(l))


if __name__ == '__main__':
    data_path = '../datasets/image_544x544/'
    f_list = glob(os.path.join(data_path, '*.jpg')) + glob(os.path.join(data_path, '*.png'))

    random.shuffle(f_list)

    n_train = 5000
    train_list = f_list[:n_train]
    val_list = f_list[n_train:]
    
    save_as_csv('list/train_list.csv', train_list)
    save_as_csv('list/val_list.csv', val_list)