import numpy as np
import cv2
from keras.models import load_model


model = load_model('keras_model.h5')
data = np.ndarray(shape=(1,224 ,224, 3), dtype=np.float32)
classes = ['coruja ','apagador','borracha','nada','robo']

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (224,224))
    image_array = np.asarray(imgS)
    normalized_image_array = (image_array.astype(np.float32)/ 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    print(prediction)
    indexVal = np.argmax(prediction)

    cv2.putText(img, str(classes[indexVal]), (50,50), cv2.FONT_HERSHEY_COMPLEX,2, (255,0,0), 2)
    print(classes[indexVal])

    cv2.imshow('img', img)
    cv2.waitKey(1)










