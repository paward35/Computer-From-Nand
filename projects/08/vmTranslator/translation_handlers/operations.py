from .helpers import pop_stack_to_d

single_operand_map = {
    'not': 'M=!M',
    'neg': 'M=-M'
}


def handle_single_operand_ops(op):
    return [
        '@SP  //{op}',
        'A=M-1',
        single_operand_map[op]
    ]


double_operand_map = {
        'add': 'M=D+M',
        'sub': 'M=M-D',
        'and': 'M=D&M',
        'or': 'M=D|M'
    }


def handle_double_op(op):
    return pop_stack_to_d(op) + [
        '@SP',
        'A=M-1',
        double_operand_map[op],
    ]

comparison_ops = {
    'eq': 'JEQ',
    'gt': 'JGT',
    'lt': 'JLT',
}

def handle_comparison_op(line):
    op = line['code'][0]
    line_num = line['num']
    return pop_stack_to_d(line) + [
        '@SP',
        'A=M-1',
        'D=M-D',
        f'@IS{op}{line_num}',
        f'D;{comparison_ops[op]}',
        '@SP',
        'A=M-1',
        'M=0',
        f'@SKIP{op}{line_num}',
        '0;JMP',
        f'(IS{op}{line_num})',
        '@SP',
        'A=M-1',
        'M=-1',
        f'(SKIP{op}{line_num})',
    ]