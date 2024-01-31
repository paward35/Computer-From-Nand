

two_operand_ops = {
        'add': 'M=D+M',
        'sub': 'M=M-D',
        'and': 'M=D&M',
        'or': 'M=D|M'
    }

def handle_two_operand_ops(op):
    return [
        '@SP   //{op}',
        'M=M-1',
        'A=M',
        'D=M',
        '@SP',
        'M=M-1',
        'A=M',
        two_operand_ops[op],
        '@SP',
        'M=M+1'
    ]

single_operand_ops = {
    'not': 'M=!M',
    'neg': 'M=-M'
}

def handle_single_operand_ops(op):
    return [
        '@SP  //{op}',
        'M=M-1',
        'A=M',
        single_operand_ops[op],
        '@SP',
        'M=M+1'
    ]


comparison_ops = {
    'eq': 'JEQ',
    'gt': 'JGT',
    'lt': 'JLT',
}

def handle_comparison_ops(op, line_num):
    return [
        '@SP  //{op}',
        'M=M-1',
        'A=M',
        'D=M',
        '@SP',
        'M=M-1',
        'A=M',
        'D=M-D',
        f'@IS{op}{line_num}',
        f'D;{comparison_ops[op]}',
        '@SP',
        'A=M',
        'M=0',
        f'@SKIP{op}{line_num}',
        '0;JMP',
        f'(IS{op}{line_num})',
        '@SP',
        'A=M',
        'M=-1',
        f'(SKIP{op}{line_num})',
        '@SP',
        'M=M+1'
    ]

def translate(line, line_num):
    if line[0] in two_operand_ops:
        return handle_two_operand_ops(line[0])
    elif line[0] in single_operand_ops:
        return handle_single_operand_ops(line[0])
    elif line[0] in comparison_ops:
        return handle_comparison_ops(line[0], line_num)
    raise Exception(f'Operation not matched! Line: {line}')