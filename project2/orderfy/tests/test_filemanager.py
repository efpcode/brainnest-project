# -*- coding: utf-8 -*-
from orderfy.filemanager import file_reader, file_maker
import pytest


def test_reading_file():
    none_existent_file = "./dasdfcfjabk.txt"
    with pytest.raises(StopIteration, match="Cannot find file"):
        next(file_reader(none_existent_file))
