import tensorflow as tf
import datetime
import numpy as np

mnist = tf.keras.datasets.mnist

def print_number(number):
	for line in number:
		for pixel in line:
			if pixel > 0:
				print('\033[92m*\033[0m', end='')
			else:
				print('0', end='')
		print()

# Loading MNIST data
(x_train, y_train),(x_test, y_test) = mnist.load_data()

for line in x_train[0]:
	print(' '.join([str(i) for i in line]))

image_to_predict = x_train[-1]
image_to_predict_class = y_train[-1]
x_train = x_train[:-1]
y_train = y_train[:-1]

# Shapes
print('Shape of X', x_train.shape)
print('Shape of Y', y_train.shape)

# Example of train data
print('Train data:')
for i in range(3):
	print_number(x_train[i])
	print('Classified as', y_train[i])

# Example of test data
print('Test data:')
for i in range(3):
	print_number(x_test[i])
	print('Classified as', y_test[i])

# Normalization
x_train, x_test = x_train / 255.0, x_test / 255.0


def create_model():
  return tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
  ])



model = create_model()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

log_dir="logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(x=x_train,
          y=y_train, 
          epochs=5, 
          validation_data=(x_test, y_test), 
          callbacks=[tensorboard_callback])

print('Predicting...')
print_number(image_to_predict)
image_to_predict = image_to_predict.reshape((1, image_to_predict.shape[0], image_to_predict.shape[1]))
answer = model.predict(image_to_predict)
print('Answer:', answer, 'Real class:', image_to_predict_class)
