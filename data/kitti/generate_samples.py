import os
import shutil


tgt_path = "../samples/"
val_list = []
with open("val_3769_imgs.txt", "r") as f:
    for line in f:
        val_list.append(line.strip('\n'))

for path in val_list:
    filename = os.path.basename(path)
    dst_path = tgt_path + filename
    print(dst_path)
    shutil.copyfile(path, dst_path)