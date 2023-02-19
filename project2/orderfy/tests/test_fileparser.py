# -*- coding: utf-8 -*-
from orderfy.fileparser import FileParser
import pytest


@pytest.fixture
def parser_obj():
    parser_data_obj = FileParser()
    return parser_data_obj
