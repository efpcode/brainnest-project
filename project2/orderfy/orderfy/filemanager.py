# -*- coding: utf-8 -*-

"""
This is module mainly used for I/O actions like read file data and other
similar actions
"""
import json
from pathlib import Path
from orderfy.fileparser import FileParser


def file_reader(path_to_file: str) -> None:
    """File reader

    Parameters
    ----------
    path_to_file : str
        The path to file with data that should be read


    Returns
    -------
    None

    """
    file_to_open = Path(path_to_file)
    line = True

    try:
        file_to_open.read_text(encoding="UTF-8")
    except FileNotFoundError as error:
        print(error)
        return "Cannot find file."
    else:
        with file_to_open.open(mode="r", encoding="UTF-8") as file_cursor:
            while line:
                line = file_cursor.readline()
                if not line:
                    break
                yield line


def file_maker(new_file_name: str, data: object):
    """

    Parameters
    ----------
    new_file_name : str
        The relative or absolute path to where file should be created.
    data : object
        The json-like object.



    Returns
    -------

    """
    new_file = Path(f"{new_file_name}.json")
    file_parser_obj = FileParser()
    parsed_data = file_parser_obj.data_parser(data)
    with new_file.open(mode="+a", encoding="utf-8") as file_json:
        file_json.write(json.dumps(parsed_data, indent=4, ensure_ascii=False))
