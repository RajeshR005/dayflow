import shutil
from pwdlib import PasswordHash
from dotenv import load_dotenv
import os
import sys
from datetime import datetime

load_dotenv()

folder_path=os.getenv("BASE_UPLOAD_FOLDER")
print(folder_path)


password_hash=PasswordHash.recommended()


def hash_password(password:str):
    return password_hash.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return password_hash.verify(plain_password,hashed_password)


"""The Below  code is used to get the file path of the media"""
def file_storage(file_name, f_name,sub_folder):

    base_dir = folder_path+sub_folder

    dt = str(int(datetime.now().timestamp()))

    try:
        os.makedirs(base_dir, mode=0o777, exist_ok=True)
    except OSError as e:
        sys.exit("Can't create {dir}: {err}".format(
            dir=base_dir, err=e))

    output_dir = base_dir + "/"

    filename = file_name.filename
    
    # Split file name and extension
    txt = filename[::-1]
    splitted = txt.split(".", 1)
    txt1 = splitted[0][::-1]
   
    files_name = f_name.split(".")

    save_full_path = f'{output_dir}{files_name[0]}{dt}.{txt1}'

    file_exe = f"uploads/{f_name}{dt}.{txt1}"
    with open(save_full_path, "wb") as buffer:
        shutil.copyfileobj(file_name.file, buffer)

    return save_full_path, file_exe