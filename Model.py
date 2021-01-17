from tensorflow import keras
import Paint
import Transform
import numpy as np

""" 
data = keras.datasets.mnist
(train_numbers, train_labels), (test_numbers, test_labels) = data.load_data()

train_numbers = train_numbers/255
test_numbers = test_numbers/255

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_numbers, train_labels, epochs=12)

print("\nPRECISÃO >>> ", model.evaluate(test_numbers, test_labels)[1])

model.save("Model/network.h5")
"""


model = keras.models.load_model("Model/network.h5")
count = 0

while True:
    Paint.main(count)
    matrix = Transform.get_pixels(count)

    if count % 2 == 0:
        print("\nPREVISÃO >>> ", np.argmax(model.predict([[matrix]])))

    count += 1
