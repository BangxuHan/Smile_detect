import os
import numpy
import cv2
from PIL import Image


# 批量修改图片尺寸，输入原图目录和修改后存放目录地址即可
def resize_batch(path, save_path):
    files = os.listdir(path)  # 返回path目录下的所有文件名
    files.sort()
    # 遍历每一张图片并修改其尺寸
    for i in files:
        document = os.path.join(path, i)  # 返回path和i拼接之后的路径，即第i张图片
        img = Image.open(document)  # 读取第i张图片
        w, h = img.size
        top = left = 0
        bottom = int(max(w - h, 0))
        right = int(max(h - w, 0))
        im = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
        padImg = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
                                    value=0)  # 上下左右要填补的像素数量，数值为0（黑边）
        new_img = Image.fromarray(cv2.cvtColor(padImg, cv2.COLOR_BGR2RGB))
        img_resize = new_img.resize((200, 200))  # 修改为200x200尺寸

        fileName = str(i)[:-4]  # 原图除后缀外的名字，这里原图后缀是.jpg
        img_resize.save(save_path + os.sep + '%s.png' % fileName)  # 保存路径，其中os.sep为系统分隔符


resize_batch('/home/kls/data/marathon_emotion/notnice', '/home/kls/data/marathon_emotion/notnice200')
