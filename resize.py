from PIL import Image
import os

# 原始文件夹路径
original_folder = '/home/kls/data/archive_new/neutral'
# 保存的新文件夹路径
new_folder = '/home/kls/data/archive_new/neutral200'

# 遍历原始文件夹中的图像
for filename in os.listdir(original_folder):
    img = Image.open(os.path.join(original_folder, filename))
    # 改变尺寸
    img_resized = img.resize((200, 200))   # 这里是你要转换的尺寸
    # 保存到新文件夹
    img_resized.save(os.path.join(new_folder, filename))
