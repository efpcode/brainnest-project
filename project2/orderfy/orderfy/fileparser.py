# -*- coding: utf-8 -*-
# import re

"""This module is mainly used data parsing and cleaning.
"""
import re


class FileParser:
    """Parses orders."""

    def data_formatter(self, key_word: str, data: str | list):
        """Cleans data and formats types"""
        if key_word == "Order Number":
            return int("".join(list(filter(lambda x: x.isdigit(), data))))

        if key_word == "Customer":
            return max(re.split(r"\s", data), key=len)

        if key_word == "Items":
            new_items = [(k, int(v)) for k, v in [i.rsplit(" ", 1) for i in data]]
            return dict(tuple(new_items))

        return None

    def data_parser(self, data: str, patterns: dict = None) -> dict:
        """Process data to certain output"""
        new_dict = {}

        if not patterns:
            patterns = {
                "Order Number": r"[A-Za-z]{1}\s[0-9]+\s[a-z]{1}",
                "Customer": r"[a-z]{1}\s[A-Z][a-z]+[0-9]+|[A-Z][a-z]+\s[a-z]{" r"1}",
                "Items": r"[A-Za-z]+\s[a-z]+\s\d",
            }

        for key, val in patterns.items():
            pattern = re.compile(val)
            parsed_data = re.findall(pattern, data)
            if key != "Items":
                parsed_data = re.search(pattern, data).group()
            data_cleared = self.data_formatter(key, parsed_data)
            new_dict.update({key: data_cleared})
        return new_dict
