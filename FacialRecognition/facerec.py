import os
import random

import cv2
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow.keras.layers import Conv2D, Dense, Flatten, Input, Layer, MaxPooling2D
from tensorflow.keras.models import Model

print("TensorFlow version:", tf.__version__)
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))