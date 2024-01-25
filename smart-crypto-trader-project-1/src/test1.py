import os
import datetime

def print_file_info():
    file_path = os.path.abspath(__file__)
    file_name = os.path.basename(file_path)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"File: {file_name}")
    print(f"Time: {current_time}")

print_file_info()
