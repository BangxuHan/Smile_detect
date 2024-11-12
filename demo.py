# 检测视频或者摄像头中的人脸
import cv2
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import dlib
from PIL import Image
import time
from models.experimental import attempt_load
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


model = load_model('models/SmileDetect.h5')
detector = dlib.get_frontal_face_detector()
# detector = attempt_load('models/yolov5s-face.pt', device)
cap = cv2.VideoCapture(
    '/mnt/marathon/师大附0713/Cam/192.168.5.11_20230713150711.mp4')
font = cv2.FONT_HERSHEY_SIMPLEX


def rec(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(gray, 1)
    if dets is not None:
        for face in dets:
            left = max(0, face.left())
            top = max(0, face.top())
            right = min(face.right(), img.shape[1])
            bottom = min(face.bottom(), img.shape[0])

            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
            img1 = cv2.resize(img[top:bottom, left:right], (150, 150))
            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            img1 = np.array(img1) / 255.
            img_tensor = img1.reshape(-1, 150, 150, 3)
            prediction = model.predict(img_tensor)
            if prediction[0][0] > 0.5:
                result = 'unsmile'
                cv2.putText(img, result, (left, top), font, 1, (0, 255, 0), 2)
            else:
                result = 'smile'
                cv2.putText(img, result, (left, top), font, 1, (0, 255, 0), 2)
                cv2.imwrite('smile/{}.jpg'.format(time.time()), img)

        cv2.imshow('Video', img)


while cap.isOpened():
    res, frame = cap.read()
    # frame = cv2.imread('test_image.jpg')
    if not res:
        break
    rec(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
