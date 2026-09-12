import os
import hashlib

def get_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return {}

    hashes = {}
    duplicates = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_hash = get_file_hash(file_path)
            if file_hash in hashes:
                duplicates.setdefault(file_hash, [hashes[file_hash]]).append(file_path)
            else:
                hashes[file_hash] = file_path
    return duplicates
