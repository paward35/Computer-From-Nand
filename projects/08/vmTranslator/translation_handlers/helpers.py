

def pop_stack_to_d(line = ''):
    if line: 
        line = '//' + str(line)
    return [
        f'@SP  {line}',
        'M=M-1',
        'A=M',
        'D=M',
    ]

def push_d_to_stack():
    return [
        '@SP',
        'M=M+1',
        'A=M-1',
        'M=D',
    ]