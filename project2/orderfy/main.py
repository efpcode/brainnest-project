# -*- coding: utf-8 -*-
"""
Runs Orderfy
"""
import argparse
from orderfy.filemanager import file_maker, file_reader


def cli_make_args(argv=None):
    """

    Parameters
    ----------
    argv : None
        Passed to make parse argument from cli

    Returns
    -------
    tuple : (str, str)
        First index is path to input file second index is path to output file.

    """
    cli_args = argparse.ArgumentParser()
    cli_args.add_argument(
        "-i",
        "--input_file",
        required=False,
        type=str,
        default="./tests/test_data/orders.txt",
        help="Path to file to read",
    )

    cli_args.add_argument(
        "-o",
        "--output_file",
        required=False,
        type=str,
        default="new_file",
        help="Path for file to be created",
    )
    return cli_args.parse_args(argv)


def main(*args):
    """Runs script"""

    file_object = file_reader(args[0])

    data = True
    while data:
        try:
            data = next(file_object)
        except StopIteration:
            return "Done"
        else:
            file_maker(args[1], data)


if __name__ == "__main__":
    input_file, output_file = cli_make_args()
    main(input_file, output_file)
