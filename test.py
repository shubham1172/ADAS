from keras.models import model_from_json
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

#load model
json_file = open('model.json', 'r')
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("model.h5")

#load image
image = cv2.imread("test1.jpg")

# pre-process the image for classification
image = cv2.resize(image, (24, 24))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)


(closed, opened) = model.predict(image)[0]
label = "Closed" if closed > opened else "Opened"
print(label)
