# Orderfy
Aim of project to be able to parse orders
and get a certain output wanted see sample below:
```json
{'Order Number': 123, 'Customer': 'John Doe', 'Items': {'Item 1': 2, 'Item 2': 1, 'Item 3': 3}}
```

# First thoughts on breaking down the project
* Need to use some sort of regex expression, so probably re/regex module
* Need fix file maker thingy
* Need to fix some sort of parser
* Need to use some sort json or jsonify module
* I/O things will be manage by pathlib
* Argparse can be used to make CLI app a bit more fun to use

# Project structure for now
Think of setting like package structure. And hopefully
this will make it easier for me to code it up.

# Potential tests
* find file - does it exist
* parse file - filter data
* format file - getting to sample output
* create file - take formatted and store it out some were on local disk.
* data set test


# Scope will not include
* No db work
* No GUI
* No web based thingy
