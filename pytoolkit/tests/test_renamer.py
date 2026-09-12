import os
from tools.renamer import rename_files

def test_rename_files_adds_prefix(tmp_path):
    f = tmp_path / "photo.jpg"
    f.write_text("data")
    rename_files(str(tmp_path), prefix="vacation_")
    assert (tmp_path / "vacation_photo.jpg").exists()

def test_rename_files_dry_run_does_not_rename(tmp_path):
    f = tmp_path / "photo.jpg"
    f.write_text("data")
    rename_files(str(tmp_path), prefix="vacation_", dry_run=True)
    assert (tmp_path / "photo.jpg").exists()
    assert not (tmp_path / "vacation_photo.jpg").exists()
