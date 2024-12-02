import os
import sys
import time
import random
import subprocess
from colorama import init
from termcolor import colored

# Hàm cài đặt thư viện nếu chưa có
def install_package(package_name):
    try:
        __import__(package_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Cài đặt các thư viện cần thiết
install_package("termcolor")
install_package("colorama")

# Hàm xóa màn hình
def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

# Danh sách màu
colors = [
    'red',
    'green',
    'blue',
    'magenta',
    'yellow',
    'cyan',
    'white'
]

# Định nghĩa các đèn màu
yellowlight = colored('o', 'yellow')
magentalight = colored('o', 'magenta')
cyanlight = colored('o', 'cyan')

lightlist = [yellowlight, cyanlight, magentalight]

# Khởi tạo colorama
init()

# Chạy chương trình hiển thị cây Giáng Sinh
while True:
    try:
        print('Merry Christmas')
        for i in range(1, 30, 2):
            tree = ''
            for j in range(i):
                randNum = random.randint(0, 500)
                if 250 <= randNum <= 750:
                    tree += lightlist[random.randint(0, 2)]
                else:
                    tree += colored('*', 'green')
            string = '_' * (15 - int(i / 2)) + tree + '_' * (15 - int(i / 2)) + '\n'
            print(string, end='')
        
        trunk = colored('mWm', 'yellow')
        for k in range(3):
            outbuffer = '_' * 14 + trunk + '_' * 14 + '\n'
            print(outbuffer, end='')

        merry_Christmas = colored('Merry Christmas', colors[random.randint(0, len(colors) - 1)])
        merry_Christmas1 = colored('Dong tran viet hoang', colors[random.randint(0, len(colors) - 1)])
        outbuffer2 = '_' * 8 + merry_Christmas + '_' * 8 + '\n'
        outbuffer3 = '_' * 8 + merry_Christmas1 + '_' * 8 + '\n'
        print(outbuffer2, end='')
        print(outbuffer3, end='')
        
        time.sleep(0.4)
        clear()
    except KeyboardInterrupt:
        print("\n Chúc bạn một Giáng Sinh vui vẻ!")
        break
