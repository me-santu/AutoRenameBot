import os

def auto_detect_name(file_path):
    base = os.path.basename(file_path)
    clean_name = base.replace("_", " ").replace(".", " ")
    return clean_name
