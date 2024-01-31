from .helpers import pop_stack_to_d, push_d_to_stack



def handle_push(line):
    segment = line['code'][1]
    segment_handler = push_handlers[segment]
    return segment_handler(line)


def handle_pop(line):
    segment = line['code'][1]
    segment_handler = pop_handlers[segment]
    return segment_handler(line)


def push_static(line):
    file = line['file']
    num = line['code'][2]
    return [
        f'@{file}.{num}   //{line}',
        'D=M',
        ] + push_d_to_stack()


def pop_static(line):
    file = line['file']
    num = line['code'][2]
    return pop_stack_to_d(line) + [
        f'@{file}.{num}',
        'M=D'
    ]


def push_pointer(line):
    selection = line['code'][2]
    this_or_that = "THIS" if selection == '0' else 'THAT'
    return [
        f'@{this_or_that}   //{line}',
        'D=M'
        ] + push_d_to_stack()

def pop_pointer(line):
    selection = line['code'][2]
    this_or_that = "THIS" if selection == '0' else 'THAT'
    return pop_stack_to_d(line) + [
        f'@{this_or_that}',
        'M=D'
    ]



def push_stndrd(line):
    vm_code = line['code']
    segment = vm_code[1]
    offset = vm_code[2]
    segment_start = "D=A" if segment == 'temp' else 'D=M'
    asm_segment = stndrd_segments[segment]

    return [
        f'@{asm_segment}   //{line}',
        segment_start,
        f'@{offset}',
        'A=D+A',
        'D=M',
        ] + push_d_to_stack()


def pop_stndrd(line):
    vm_code = line['code']
    segment = vm_code[1]
    offset = vm_code[2]
    segment_start = "D=A" if segment == 'temp' else 'D=M'
    asm_segment = stndrd_segments[segment]
    
    return [
        f'@{asm_segment}   //{line}',
        segment_start,
        f'@{offset}',
        'D=D+A',
        '@SP',
        'M=M-1',
        'A=M+1',
        'M=D',
        'A=A-1',
        'D=M',
        'A=A+1',
        'A=M',
        'M=D',
    ]


stndrd_segments = {
    'local': 'LCL',
    'argument': 'ARG',
    'this': 'THIS',
    'that': 'THAT',
    'temp': '5',
}


def push_constant(line):
    offset = line['code'][2]
    return [
        f'@{offset}   //{line}',
        'D=A'] + push_d_to_stack()

push_handlers = {
    'local': push_stndrd,
    'argument': push_stndrd,
    'this': push_stndrd,
    'that': push_stndrd,
    'temp': push_stndrd,
    'constant': push_constant,
    'pointer': push_pointer,
    'static': push_static,
} 


pop_handlers = {
    'local': pop_stndrd,
    'argument': pop_stndrd,
    'this': pop_stndrd,
    'that': pop_stndrd,
    'temp': pop_stndrd,
    'pointer': pop_pointer,
    'static': pop_static,
} 