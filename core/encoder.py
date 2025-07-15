"""
Setting up the basic groundwork for the project in this file.
Going to start by loading MNIST through Tensorflow as our "testing" 
set
"""

import tensorflow as tf


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_test.shape)