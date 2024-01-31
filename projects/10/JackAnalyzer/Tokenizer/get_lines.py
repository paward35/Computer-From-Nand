import os
import re
import shlex

def remove_comments(text):
    pattern = r"(\/\/.*?\n|\/\*.*?\*\/)"
    return re.sub(pattern, "", text, flags=re.DOTALL)


def add_spaces_around_symbols(code):
    for symbol in "()[]{},;=.+-*/&|~<>":
        code = code.replace(symbol, f" {symbol} ")
    return code


def format_line(line):
    line = line.replace("\n", "")
    line = line.replace("\t", "")
    line = line.partition("//")[0]
    line = line.rstrip()
    line = line.lstrip()
    return line


def format_tokens(code):
    return [format_line(line) for line in code]

def format_files_code(files):
    for file in files:
        file['code'] = remove_comments(file['code'])
        file['code'] = add_spaces_around_symbols(file['code'])
        file['tokens'] = shlex.split(file['code'])
        file['tokens'] = format_tokens(file['tokens'])
        file['tokens'] = remove_nulls(file['tokens'])
    return files


def get_lines_from_file(path):
    with open(path, 'r') as file:
        return file.read()

def remove_nulls(lines):
    return list(filter(lambda line: line, lines))


def get_jack_file_name(path):
    name = path.split('/')[-1].split('.')[-2]
    return name


def get_jack_files_from_dir(dir):
    file_paths = [os.path.join(dir, file) for file in os.listdir(dir)]
    jack_file_paths = filter(lambda file: file.endswith(".jack"), file_paths)
    return list(jack_file_paths)


def read_lines_from_files(files):
    files_with_lines = []
    for file in files:
        lines = get_lines_from_file(file)
        new_file = {
            'code': lines,
            'file': file
        }
        files_with_lines.append(new_file)
    return files_with_lines


def get_files_for_processing(path):
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        return get_jack_files_from_dir(path)
    else:
        current_dir = os.path.dirname(os.path.realpath(__file__))
        return get_jack_files_from_dir(current_dir)



def read_and_preprocess(path):
    files_paths = get_files_for_processing(path)
    files = read_lines_from_files(files_paths)
    return format_files_code(files)

