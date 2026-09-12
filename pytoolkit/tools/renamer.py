import os

def rename_files(folder_path, prefix="", suffix="", ext_filter=None):
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if not os.path.isfile(file_path):
            continue
        name, ext = os.path.splitext(filename)
        if ext_filter and ext.lower() != ext_filter.lower():
            continue
        new_name = f"{prefix}{name}{suffix}{ext}"
        new_path = os.path.join(folder_path, new_name)
        os.rename(file_path, new_path)
        print(f"Renamed: {filename} -^> {new_name}")
