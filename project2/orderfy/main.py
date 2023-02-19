# -*- coding: utf-8 -*-
"""
Runs Orderfy
"""
from orderfy.fileparser import FileParser
from orderfy.filemanager import file_maker, file_reader


def main():
    """Runs script"""
    file_parser = FileParser()
    file_object = file_reader("./tests/test_data/orders.txt")
    for data in file_object:
        file_maker("test-json", file_parser.data_parser(data))


if __name__ == "__main__":
    main()
