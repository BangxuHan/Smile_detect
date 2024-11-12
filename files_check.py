import os

root = '/home/kls/data/genki4k/files2/'
train_dir = root + 'train/'
validation_dir = root + 'validation/'
test_dir = root + 'test/'

train_smile_dir = train_dir + 'smile/'
train_umsmile_dir = train_dir + 'unsmile/'
validation_smile_dir = validation_dir + 'smile/'
validation_unsmile_dir = validation_dir + 'unsmile/'
test_smile_dir = test_dir + 'smile/'
test_umsmile_dir = test_dir + 'unsmile/'


print('total training smile images:', len(os.listdir(train_smile_dir)))
print('total training unsmile images:', len(os.listdir(train_umsmile_dir)))
print('total testing smile images:', len(os.listdir(test_smile_dir)))
print('total testing unsmile images:', len(os.listdir(test_umsmile_dir)))
print('total validation smile images:', len(os.listdir(validation_smile_dir)))
print('total validation unsmile images:', len(os.listdir(validation_unsmile_dir)))
