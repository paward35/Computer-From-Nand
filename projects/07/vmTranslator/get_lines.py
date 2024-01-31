import sys

def get_lines_from_file(path):
    with open(path, 'r') as file:
        return file.readlines()
    
def format_line(line):
    line = line.rstrip()
    line = line.replace("\n", "")
    line = line.partition("//")[0]
    return line


def format_lines(file):
    lines = []
    for line in file:
        line = format_line(line)
        lines.append(line)
    lines = remove_nulls(lines)
    return lines


def read_lines_from_file(path):
    with open(path, 'r') as file:
        return file.readlines()

def remove_nulls(lines):
    return list(filter(lambda line: line, lines))

def read_and_preprocess(file_name):
    lines = read_lines_from_file(file_name)
    return format_lines(lines)
