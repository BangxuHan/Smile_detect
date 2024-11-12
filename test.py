# 单张图片进行判断  是笑脸还是非笑脸
import numpy as np
from keras.models import load_model
from keras.utils import image_utils

# 加载模型
model = load_model('models/SmileDetect.h5')
# 本地图片路径
img_path = 'test/smile01.jpg'
img = image_utils.load_img(img_path, target_size=(150, 150))

img_tensor = image_utils.img_to_array(img) / 255.0
img_tensor = np.expand_dims(img_tensor, axis=0)
prediction = model.predict(img_tensor)
print(prediction)
if prediction[0][0] > 0.7:
    result = '非笑脸'
else:
    result = '笑脸'
print(result)
