from keras.preprocessing.image import ImageDataGenerator
# 数据增强后图片变化
import matplotlib.pyplot as plt
# This is module with image preprocessing utilities
# from keras.preprocessing import image
from keras.utils import image_utils
import os

# 数据增强
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

# train_smile_dir = '/home/kls/data/genki4k/files2/train/smile'
#
# fnames = [os.path.join(train_smile_dir, fname) for fname in os.listdir(train_smile_dir)]
# img_path = fnames[3]
# img = image_utils.load_img(img_path, target_size=(150, 150))
# x = image_utils.img_to_array(img)
# x = x.reshape((1,) + x.shape)
# i = 0
# for batch in datagen.flow(x, batch_size=1):
#     plt.figure(i)
#     imgplot = plt.imshow(image_utils.array_to_img(batch[0]))
#     i += 1
#     if i % 4 == 0:
#         break
# plt.show()
