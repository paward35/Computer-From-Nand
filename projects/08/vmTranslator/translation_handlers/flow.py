from .helpers import pop_stack_to_d

def handle_label(line):
    label = line['code'][1]
    return [
        f'({label})   //{line}'
    ]

def handle_goto(line):
    instruction = line['code'][0]
    label = line['code'][1]
    if ('if' not in instruction):
        return [
            f'@{label}   //{line}',
            '0;JMP'
        ]
    
    return pop_stack_to_d(line) + [
        f'@{label}',
        'D;JNE'
    ]

def handle_flow(line):
    instruction = line['code'][0]
    if 'goto' in instruction:
        return handle_goto(line)
    elif instruction == 'label':
        return handle_label(line)
    else:
        raise Exception(f'Unhandled operator in handle_flow line: {line}')
