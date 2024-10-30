import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0' #Desactiva Aviso indefinido
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' #Desactiva Aviso de que aprovechará tu CPU para obtener esa velocidad adicional.

import keras as ks
import tensorflow as tf
import numpy as np
#/*
#print(tf.add(1, 2))
#print(tf.add([1, 2], [3, 4]))
#print(tf.square(5))
#print(tf.reduce_sum([1, 2, 3]))

# Operator overloading is also supported
#print(tf.square(2) + tf.square(3))
#*/

#/*
ndarray = np.ones([3, 3])

tf.convert_to_tensor(ndarray, dtype=tf.float32)

print("TensorFlow operations convert numpy arrays to Tensors automatically")
tensor = tf.multiply(ndarray, 42)
print(tensor)

print("And NumPy operations convert Tensors to numpy arrays automatically")
print(np.add(tensor, 1))

print("The .numpy() method explicitly converts a Tensor to a numpy array")
print(tensor.numpy())
#*/