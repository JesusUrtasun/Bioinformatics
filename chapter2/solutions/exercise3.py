# Exercise 3: Get used to python
# Author: Jesús Urtasun - 2020/21 

# Import basic libraries
import numpy as np
import tensorflow as tf
import keras
# TensorFlow logger function to avoid warnings
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# Operations with numpy
print("\nOperations with numpy")
a = np.random.random((2, 3))
b = np.random.random((3, 2))
c = np.dot(a, b)
print("a =\n{}\nb =\n{}\na · b =\n{}".format(a, b, c))

# Check version of tensorflow
print("\nTensorflow version: {}".format(tf.__version__))

# Build a model with keras
print("\nBuilding model with Keras")
model = keras.Sequential()
print(model)
# End of the checks
print("\nEverything up to date")