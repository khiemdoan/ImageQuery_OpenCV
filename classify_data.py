
import os
from shutil import copyfile

folder_path = input('Enter images data folder : ')
data_folder = os.path.join(folder_path, 'data')
test_folder = os.path.join(folder_path, 'test')

# tạo thư mục data
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# tạo thư mục test
if not os.path.exists(test_folder):
    os.makedirs(test_folder)

# chia các file trong thư mục hiện tại ra 2 nhóm
for item in os.listdir(folder_path):
    file_path = os.path.join(folder_path, item)
    if os.path.isfile(file_path):
        file_name = os.path.splitext(item)[0]
        number = int(file_name)
        du = number % 100
        if 0 <= du < 75:
            new_file_path = os.path.join(data_folder, item)
            copyfile(file_path, new_file_path)
        else:
            new_file_path = os.path.join(test_folder, item)
            copyfile(file_path, new_file_path)
