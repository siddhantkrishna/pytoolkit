import os
import shutil
from tools.organizer import organize_folder

def test_organize_folder_creates_ext_dirs(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("hello")
    organize_folder(str(tmp_path))
    assert (tmp_path / "txt" / "test.txt").exists()
