import os


def format_line(line):
    line = line.replace("\n", "")
    line = line.replace("\t", "")
    line = line.partition("//")[0]
    line = line.rstrip()
    line = line.lstrip()
    return line


def format_lines(lines):
    for num, line in enumerate(lines):
        line['code'] = format_line(line['code'])
        line['num'] = str(num)
    lines = remove_nulls(lines)
    return lines


def get_lines_from_file(path):
    file_name = get_vm_file_name(path)
    result = []
    with open(path, 'r') as file:
        file_contents = file.readlines()
        for line in file_contents:
            result.append({'code': line, 'file': file_name}) 
    return result

def remove_nulls(lines):
    return list(filter(lambda line: line['code'], lines))


def get_vm_file_name(path):
    name = path.split('/')[-1].split('.')[-2]
    return name


def get_vm_file_paths(dir):
    file_paths = [os.path.join(dir, file) for file in os.listdir(dir)]
    vm_file_paths = filter(lambda file: file.endswith(".vm"), file_paths)
    return list(vm_file_paths)

def get_lines_from_files(path):
    lines_from_files = []
    file_paths = get_vm_file_paths(path)
    for path in file_paths:
        lines_from_files = lines_from_files + get_lines_from_file(path)
    lines_from_files =  [{'code': 'call Sys.init 0', 'file': 'Sys'}] + lines_from_files
    return lines_from_files

def get_lines_from_current_dir(path):
    return []

def read_lines(path):
    if os.path.isfile(path):
        result = get_lines_from_file(path)
    elif os.path.isdir(path):
        result = get_lines_from_files(path)
    else:
        current_dir = os.getcwd()
        result = get_lines_from_files(current_dir)
    return result


def get_result_file_name(path):
    if is_dir(path):
        folder_name = path.split('/')[-1]
        return os.getcwd() + '/' +  path + f'/{folder_name}.asm'
    else:
        return os.getcwd() + '/' + path.replace('.vm', '.asm')
    

def is_dir(path):
    return not path.endswith('.vm')


def get_files_for_processing(path):
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        return get_file_paths(path)
    else:
        current_dir = os.getcwd()
        return get_file_paths(current_dir)



def read_and_preprocess(path):
    files = get_files_for_processing(path)
    lines = read_lines_from_files(files)
    return format_lines(lines)
