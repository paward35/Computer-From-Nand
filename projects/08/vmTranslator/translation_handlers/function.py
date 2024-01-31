from .helpers import push_d_to_stack, pop_stack_to_d

def handle_call(line):
    vm_code = line['code']
    name = vm_code[1]
    num_args = int(vm_code[2])
    line_number = line['num']
    return [
        f'@returnAddress{name}.{line_number}     // {line}',
        'D=A'] + push_d_to_stack() + [  
        '@LCL',
        'D=M'] + push_d_to_stack() + [
        '@ARG',
        'D=M'] + push_d_to_stack() + [
        '@THIS',
        'D=M'] + push_d_to_stack() + [
        '@THAT',
        'D=M'] + push_d_to_stack() + [
        '@SP',
        'D=M',
        '@5',
        'D=D-A',
        f'@{num_args}',
        'D=D-A',
        '@ARG',
        'M=D',
        '@SP',
        'D=M',
        '@LCL',
        'M=D',
        f'@{name}',
        '0;JMP',
        f'(returnAddress{name}.{line_number})'
    ]


def handle_function(line):
    vm_code = line['code']
    name = vm_code[1]
    num_local_vars = int(vm_code[2])

    result = [f"({name})"]
    for i in range(num_local_vars):
        result = result + [
            '@SP',
            'M=M+1',
            'A=M-1',
            'M=0'
        ]
    result[0] = result[0] + f"//{line}"
    return result


def handle_return(line):
    return [
        f'@LCL  //{line}', #Frame = LCL
        'D=M',
        '@FRAME',
        'M=D',
        '@5',              #RET = *(FRAME-5)
        'D=D-A',
        'A=D',
        'D=M',
        '@RET',
        'M=D' ] + pop_stack_to_d() + [
        '@ARG',
        'A=M',
        'M=D',
        '@ARG', #SP = ARG+1
        'D=M+1',  
        '@SP',
        'M=D',
        '@FRAME',
        'M=M-1',
        'A=M',
        'D=M',
        '@THAT',
        'M=D',
        '@FRAME',
        'M=M-1',
        'A=M',
        'D=M',
        '@THIS',
        'M=D',
        '@FRAME',
        'M=M-1',
        'A=M',
        'D=M',
        '@ARG',
        'M=D',
        '@FRAME',
        'M=M-1',
        'A=M',
        'D=M',
        '@LCL',
        'M=D',
        '@RET',
        'A=M',
        '0;JMP'
    ]
