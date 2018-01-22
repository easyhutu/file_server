"""
CREAt: 2018/1/19
AUTHOR: Hehahutu
"""
import sys

DEBUG = False
SECRET_KEY = 'SDF6(()%fln(%$)blh&$#hnmuk$hgk79g^$*n5JN'

# 配置服务器读取文件根目录
try:
    env_platform = sys.platform
    if env_platform == 'linux':
        # linux 系统配置
        FILE_BASE_PATH = '/extend/fileserver'
    else:
        # window 文件目录配置
        FILE_BASE_PATH = 'E:\\file_server\\TEST'
except:
    # 获取异常，默认用Linux
    FILE_BASE_PATH = '/extend/fileserver'
