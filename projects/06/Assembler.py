import sys
import mapping 


def format_line(line):
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    line = line.partition("//")[0]
    return line


def format_lines(file):
    lines = []
    for line in file:
        line = format_line(line)
        lines.append(line) 
    return lines


def get_lines_from_file(path):
    with open(path, 'r') as file:
        return file.readlines()

def remove_nulls(lines):
    return list(filter(lambda line: line, lines))


def is_A_instruction(line):
    return line[0] == '@'


def convert_A_instruction(line):
    val = int(line[1:])
    binary = f'{val:016b}'
    return binary


def tokanize_C_instruction(line):
    dest, jump, comp = "", "", ""
    if '=' in line: 
        dest = line.partition('=')[0]
        line = line.partition('=')[2]
    if ';' in line: 
        jump = line.partition(';')[2]
        comp = line.partition(';')[0]
    else:
        comp = line
    return dest, jump, comp


def convert_C_instruction(line):
    dest, jump, comp = tokanize_C_instruction(line)
    dest_bin = mapping.dest[dest]
    jump_bin = mapping.jump[jump]
    comp_bin = mapping.comp[comp]
    return f"111{comp_bin}{dest_bin}{jump_bin}"


def convert_to_binary_instructions(lines):
    for idx, line in enumerate(lines): 
        if is_A_instruction(line):
            lines[idx] = convert_A_instruction(line)
        else: 
            lines[idx] = convert_C_instruction(line)
    return lines


def add_labels(lines):
    symbols = mapping.symbols
    new_lines = []
    lattest_symbol = 16
    for line in lines:
        if line[0] == '(':
            symbol = line[1:-1]
            symbols[symbol] = f"{len(new_lines)}"
        else:
            new_lines.append(line)
    return new_lines, symbols

def contains_variable(line):
    try:
        int(line[1:])
        return False
    except ValueError:
        return True

def replace_variables(lines, symbols):
    variable_counter = 16
    for idx, line in enumerate(lines):
        if is_A_instruction(line) and contains_variable(line):
            variable_name = line[1:]
            if variable_name not in symbols:
                symbols[variable_name] = f"{variable_counter}"
                variable_counter += 1
            lines[idx] = f"@{symbols[variable_name]}"
    return lines

def remove_symbols(lines):
    lines, symbols = add_labels(lines)
    lines = replace_variables(lines, symbols)
    return lines


lines = get_lines_from_file(sys.argv[1])
lines = format_lines(lines)
lines = remove_nulls(lines)
lines = remove_symbols(lines)
lines = convert_to_binary_instructions(lines)

file_name = sys.argv[1].split('.')[0]

with open(f"{file_name}.hack", "w") as outfile:
    outfile.write("\n".join(lines))



