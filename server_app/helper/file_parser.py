"""
CREAt: 2018/1/19
AUTHOR: Hehahutu
"""
from setting import FILE_BASE_PATH
import os

# 读取文件核心函数， file_path参数实例 ： /xxx/xxx & /xx/xx.xx
def get_file_list(file_path):
    try:
        # join完整路径
        path = os.path.join(FILE_BASE_PATH, file_path)
        # path = FILE_BASE_PATH + file_path
        # print(file_path)
        # 判断路径是否存在
        if os.path.exists(path):
            # 判断路径是文件夹
            if os.path.isdir(path):
                # 获取路径下的所有文件名和文件夹名
                file_or_folder_list = os.listdir(path)
                file_list = []
                folder_list = []
                # 遍历获取的列表， 构建文件参数
                for item in file_or_folder_list:
                    add_path = ('/' + file_path + '/' + item) if file_path else item
                    if os.path.isfile(os.path.join(path, item)):

                        file_list.append([item, add_path])
                    else:
                        folder_list.append([item, add_path])
                # 返回的参数 folder 文件夹标识， file_list 文件列表， folder_list 文件夹列表
                return 'folder', file_list, folder_list
            # 判断路径是文件
            elif os.path.isfile(path):
                # 使用basename方法获取文件名
                filename = os.path.basename(path)
                # 读取文件
                with open(path, 'rb') as f:
                    data = f.read()
                # 返回参数 file 文件标识， filename 文件名， data读取的二进制文件内容
                return 'file', filename, data
        else:
            return None
    except Exception as e:
        return None
