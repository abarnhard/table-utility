'''Utility to convert invalid db column names for SQLAlchemy'''

from os.path import abspath, dirname, join

_CWD = dirname(abspath(__file__))
INPUT_FILE_NAME = 'to_convert.txt'
OUTPUT_FILE_NAME = 'converted.txt'

input_file = open(join(_CWD, INPUT_FILE_NAME))
target_file = open(join(_CWD, OUTPUT_FILE_NAME), 'w+')
target_file.truncate()

for line in iter(input_file):
    parts = line.split('=')
    parts = [part.strip() for part in line.split("=")]

    column_name_replacement = "Column('{0}', ".format(parts[0])

    parts[1] = parts[1].replace('Column(', column_name_replacement)
    parts[0] = parts[0].lower()

    finished_line = ' = '.join(parts)
    finished_line = finished_line.join(['    ', "\n"])
    target_file.write(finished_line)

input_file.close()
target_file.close()
