"""
CREAt: 2018/1/19
AUTHOR: Hehahutu
"""
from setting import FILE_BASE_PATH
import os

# 获取文件核心函数
"""

"""
def get_file_list(file_path):
    path = os.path.join(FILE_BASE_PATH, file_path)
    # path = FILE_BASE_PATH + file_path
    # print(file_path)
    if os.path.exists(path):
        if os.path.isdir(path):
            file_or_folder_list = os.listdir(path)
            file_list = []
            folder_list = []
            for item in file_or_folder_list:
                add_path = ('/'+file_path + '/' + item) if file_path else item
                if os.path.isfile(os.path.join(path, item)):

                    file_list.append([item, add_path])
                else:
                    folder_list.append([item, add_path])
            return 'folder', file_list, folder_list
        elif os.path.isfile(path):
            filename = os.path.basename(path)
            with open(path, 'rb') as f:
                data = f.read()
            return 'file', filename, data
    else:
        return None
