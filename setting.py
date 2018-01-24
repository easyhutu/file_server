"""
CREAt: 2018/1/19
AUTHOR: Hehahutu
"""
import sys
import dotenv
import os
from getenv import env

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))  # This directory
try:
    dotenv_path = os.path.join(PROJECT_ROOT, '.env')
    dotenv.read_dotenv(dotenv_path)
except Exception as e:
    print('没有读取到本地环境变量配置，将使用预置的环境变量')
    print(e)
DEBUG = env('DEBUG', False)
SECRET_KEY = 'SDF6(()%fln(%$)blh&$#hnmuk$hgk79g^$*n5JN'
BLANK_SIZE = 512

# 配置服务器读取文件根目录
LINUX_BASE_PATH = [
    '/extend/fileserver',

]
WINDOW_BASE_PATH = [
    'E:\\file_server\\TEST',
    'E:\\file_server\\TEST',
]
try:
    env_platform = sys.platform
    if env_platform == 'linux':
        # linux 系统配置
        FILE_BASE_PATH = LINUX_BASE_PATH
    else:
        # window 文件目录配置
        FILE_BASE_PATH = WINDOW_BASE_PATH
except:
    # 获取异常，默认用Linux
    FILE_BASE_PATH = LINUX_BASE_PATH
