import os
from tools.duplicate_finder import find_duplicates

def test_find_duplicates_detects_same_content(tmp_path):
    f1 = tmp_path / "a.txt"
    f2 = tmp_path / "b.txt"
    f1.write_text("same content")
    f2.write_text("same content")
    dupes = find_duplicates(str(tmp_path))
    assert len(dupes) == 1

def test_find_duplicates_no_dupes_for_unique_files(tmp_path):
    f1 = tmp_path / "a.txt"
    f2 = tmp_path / "b.txt"
    f1.write_text("content one")
    f2.write_text("content two")
    dupes = find_duplicates(str(tmp_path))
    assert len(dupes) == 0
