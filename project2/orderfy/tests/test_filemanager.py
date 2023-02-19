# -*- coding: utf-8 -*-
from orderfy.filemanager import file_reader, file_maker
import pytest


def test_reading_no_file():
    none_existent_file = "./dasdfcfjabk.txt"
    with pytest.raises(StopIteration, match="Cannot find file"):
        next(file_reader(none_existent_file))


def test_read_file():
    file_obj = file_reader("./test_data/test.txt")
    expected_values = ["Start", "ABCD", 1234, "abc123", "End"]
    for idx, line in enumerate(file_obj):
        assert line == f"{expected_values[idx]}\n"
