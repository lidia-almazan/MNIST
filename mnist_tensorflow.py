# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:10:27 2020

TensorFlow MNIST

@author: Lidia
"""

#import relevant packages
import numpy as np
import tensorflow as tf

import tensorflow_datasets as tfds

#data
mnist_dataset, mnist_info = tfds.load(name='mnist', with_info=True, as_supervised=True)

mnist_dataset