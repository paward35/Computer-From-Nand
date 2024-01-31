
def is_constant(line):
    return line[1] == 'constant'


stndrd_segments = {
    'local': 'LCL',
    'argument': 'ARG',
    'this': 'THIS',
    'that': 'THAT',
    'temp': '5',
}


def trans_constant(line):
    return [
        f'@{line[2]}   //{line}',
        'D=A',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1'
        ]


def is_stndrd_segments(line):
    return line[1] in stndrd_segments


def trans_stndrd_segments(line):
    if line[0] == 'push':
        return gen_push_stndrd(line)
    elif line[0] == 'pop':
        return gen_pop_stndrd(line)
    raise Exception(f'Not push or pop in line: {line}')


def trans_pointer(line):
    if line[0] == 'push':
        return gen_push_pointer(line)
    elif line[0] == 'pop':
        return gen_pop_pointer(line)
    raise Exception(f'Not push or pop in line: {line}')


def trans_static(file_name, line):
    file_name = file_name.replace('/', '')
    if line[0] == 'push':
        return gen_push_static(file_name, line)
    elif line[0] == 'pop':
        return gen_pop_static(file_name, line)
    raise Exception(f'Not push or pop in line: {line}')


def gen_push_static(file_name, line):
    return [
        f'@{file_name}.{line[2]}   //{line}',
        'D=M',
        f'@SP',
        'M=M+1',
        'A=M',
        'A=A-1',
        'M=D'
        ]


def gen_pop_static(file_name, line):
    return [
        f'@SP   //{line}',
        'M=M-1',
        'A=M',
        'D=M',
        f'@{file_name}.{line[2]}',
        'M=D'
    ]


def gen_push_pointer(line):
    this_or_that = "THIS" if line[2] == '0' else 'THAT'
    return [
        f'@{this_or_that}   //{line}',
        'D=M',
        f'@SP',
        'M=M+1',
        'A=M',
        'A=A-1',
        'M=D'
        ]

def gen_pop_pointer(line):
    this_or_that = "THIS" if line[2] == '0' else 'THAT'
    return [
        f'@SP   //{line}',
        'M=M-1',
        'A=M',
        'D=M',
        f'@{this_or_that}',
        'M=D'
    ]


def gen_pop_stndrd(line):
    line_2 = "D=A" if line[1] == 'temp' else 'D=M'
    return [
        f'@{stndrd_segments[line[1]]}   //{line}',
        line_2,
        f'@{line[2]}',
        'D=D+A',
        '@SP',
        'A=M',
        'M=D',
        'A=A-1',
        'D=M',
        'A=A+1',
        'A=M',
        'M=D',
        '@SP',
        'M=M-1'
    ]


def gen_push_stndrd(line):
    line_2 = "D=A" if line[1] == 'temp' else 'D=M'
    return [
        f'@{stndrd_segments[line[1]]}   //{line}',
        line_2,
        f'@{line[2]}',
        'A=D+A',
        'D=M',
        '@SP',
        'M=M+1',
        'A=M',
        'A=A-1',
        'M=D'
        ]


def is_pointer(line):
    return line[1] == 'pointer'


def is_static(line):
    return line[1] == 'static'


def translate(file_name, line):
    result = []
    if is_stndrd_segments(line):
        return trans_stndrd_segments(line)
    elif is_constant(line):
        return trans_constant(line)
    elif is_pointer(line):
        return trans_pointer(line)
    elif is_static(line):
        return trans_static(file_name, line)
    raise Exception(f'Not handled operator in line: {line}')