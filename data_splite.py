import os
import shutil

# 原始数据集路径
original_dataset_dir = '/home/kls/data/genki4k/files1'

# 新的数据集
base_dir = '/home/kls/data/genki4k/files2'
# os.mkdir(base_dir)
#
# # 训练图像、验证图像、测试图像的目录
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')

train_cats_dir = os.path.join(train_dir, 'smile')
train_dogs_dir = os.path.join(train_dir, 'unsmile')
validation_cats_dir = os.path.join(validation_dir, 'smile')
validation_dogs_dir = os.path.join(validation_dir, 'unsmile')
test_cats_dir = os.path.join(test_dir, 'smile')
test_dogs_dir = os.path.join(test_dir, 'unsmile')

# os.mkdir(train_dir)
# os.mkdir(validation_dir)
# os.mkdir(test_dir)

# os.mkdir(train_cats_dir)
# os.mkdir(train_dogs_dir)
# os.mkdir(validation_cats_dir)
# os.mkdir(validation_dogs_dir)
# os.mkdir(test_cats_dir)
# os.mkdir(test_dogs_dir)

# 复制笑脸图片
fnames = ['file{}.jpg'.format(str(i).zfill(4)) for i in range(1, 1501)]
for fname in fnames:
    try:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(train_cats_dir, fname)
        shutil.copyfile(src, dst)
    except:
        continue

fnames = ['file{}.jpg'.format(i) for i in range(1501, 1801)]
for fname in fnames:
    try:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(validation_cats_dir, fname)
        shutil.copyfile(src, dst)
    except:
        continue

fnames = ['file{}.jpg'.format(i) for i in range(1801, 2101)]
for fname in fnames:
    try:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(test_cats_dir, fname)
        shutil.copyfile(src, dst)
    except:
        continue

# 复制非笑脸图片
fnames = ['file{}.jpg'.format(i) for i in range(2201, 3701)]
for fname in fnames:
    try:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(train_dogs_dir, fname)
        shutil.copyfile(src, dst)
    except:
        continue

fnames = ['file{}.jpg'.format(i) for i in range(3701, 4001)]
for fname in fnames:
    try:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(validation_dogs_dir, fname)
        shutil.copyfile(src, dst)
    except:
        continue

fnames = ['file{}.jpg'.format(i) for i in range(3701, 4001)]
for fname in fnames:
    try:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(test_dogs_dir, fname)
        shutil.copyfile(src, dst)
    except:
        continue