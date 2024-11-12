# import cv2
#
# img = cv2.imread('test/test.jpeg')
# faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# faces = faceCascade.detectMultiScale(img, 1.15)
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyWindow()


import numpy as np
import cv2

# read th image
with open("test/test_image.jpg", "rb") as image:
    f = image.read()

    # convert to numpy array
    image = np.asarray(bytearray(f))

    # RGB to Grayscale
    image = cv2.imdecode(image, 1)

    cv2.rectangle(image, (831, 853), (1307, 1445), (0, 255, 0), 2, lineType=cv2.LINE_AA)

    # display image
    image = cv2.resize(image, None, fx=0.5, fy=0.5)

    cv2.imshow('video', image)
    cv2.waitKey(0)
