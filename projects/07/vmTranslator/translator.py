import translate_logic
import translate_mem

def is_logic(line):
    return len(line) == 1

def is_mem(line):
    return len(line) == 3


def translate(file_name, vm_code):
    result = []
    for line_num, line in enumerate(vm_code):
        if is_logic(line):
            result += translate_logic.translate(line, line_num)
        else:
            result += translate_mem.translate(file_name, line)
    return result