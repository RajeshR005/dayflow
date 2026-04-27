import shutil
from pwdlib import PasswordHash
from dotenv import load_dotenv
import os
import sys
from datetime import datetime

load_dotenv()

BASE_UPLOAD_FOLDER = os.getenv(
    "UPLOAD_DIR",
    os.path.join(os.getcwd(), "dayflow_uploads")
)
os.makedirs(BASE_UPLOAD_FOLDER, exist_ok=True)



password_hash=PasswordHash.recommended()


def hash_password(password:str):
    return password_hash.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return password_hash.verify(plain_password,hashed_password)


"""The Below  code is used to get the file path of the media"""
def file_storage(file_name, f_name,sub_folder):

    base_dir = os.path.join(BASE_UPLOAD_FOLDER, sub_folder)
    os.makedirs(base_dir, exist_ok=True)
    dt = str(int(datetime.now().timestamp()))

    # Unique timestamp
    dt = str(int(datetime.now().timestamp()))

    # Get extension safely
    original = file_name.filename
    ext = original.split(".")[-1]

    name_without_ext = f_name.split(".")[0]

    new_filename = f"{name_without_ext}_{dt}.{ext}"

    save_full_path = os.path.join(base_dir, new_filename)

    # What you store in DB (relative path)
    file_exe = f"{sub_folder}/{new_filename}"

    with open(save_full_path, "wb") as buffer:
        shutil.copyfileobj(file_name.file, buffer)

    return save_full_path, file_exe