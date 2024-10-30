import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0' #Desactiva Aviso indefinido
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' #Desactiva Aviso de que aprovechará tu CPU para obtener esa velocidad adicional.

import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
faharenheit = np.array([-40, 14, 32, 45, 59, 72, 100], dtype=float)

oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.01),
    loss = "mean_squared_error"
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, faharenheit, epochs=300, verbose=False)
print("Modelo Entrenado")

#tensorflowjs_converter --input_format keras Modelo.h5 PaginaWeb(Capeta creada con mkdir nombre)

modelo.save("Modelo.h5")