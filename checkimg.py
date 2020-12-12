# -*- coding: utf-8 -*-
"""
reference:
https://blog.csdn.net/kingroc/article/details/86692156
"""
import os

train_dir = './dataset_whole/(50000,100000]/'


def is_valid_jpg(jpg_file):
    with open(jpg_file, 'rb') as f:
        f.seek(-2, 2)
        buf = f.read()
        f.close()
        return buf ==  b'\xff\xd9'  # 判定jpg是否包含结束字段

data_size = len([lists for lists in os.listdir(train_dir) if os.path.isfile(os.path.join(train_dir, lists))])
# recv_size = 0
incompleteFile = 0
print('file size : %d' % data_size)

print(os.listdir(train_dir))

for file in os.listdir(train_dir):
    # print(imgs)
    imgname =str(file[:-4])
    # print(imgname)
    imgint = int(imgname)
# =============================================================================
#     for imgs in os.makedirs(folders):
#         print(imgs)
# =============================================================================
    if os.path.splitext(file)[1].lower() == '.jpg':
        ret = is_valid_jpg(train_dir + file)
        if ret == False:
            incompleteFile = incompleteFile + 1
            os.remove(train_dir + file)
            print('\nincomplete file : %d' % imgint)
print('\n total # incomplete file : %d' % incompleteFile)
