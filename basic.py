import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

print(tf.__version__)

# Tensor
tensorA = tf.constant(8)
print(tensorA)

tensorA = tf.constant(8.8)
print(tensorA)

# shape
tensorA = tf.constant(8, shape=(1, 1))
print(tensorA)

tensorA = tf.constant([[10,20,30], [40,50,60]], shape=(3,2))
print(tensorA)

#dtype
tensorA = tf.constant(8, shape=(1,1), dtype = tf.float32)
print(tensorA)

#matrix
tensorA = tf.ones((4,4))
print(tensorA)

#matrix
tensorA = tf.zeros((4,4))
print(tensorA)

#identity matrix 
tensorA = tf.eye(5)
print(tensorA)