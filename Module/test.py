import shutil
import os
from time import sleep
def clean_temp_file(file_path):
    if os.path.isdir(file_path):
        shutil.rmtree(file_path)
        os.mkdir(file_path)
    else:
        os.mkdir(file_path)


clean_temp_file('.\\module\\test')