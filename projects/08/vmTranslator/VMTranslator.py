import sys
import get_lines
import tokanizer
import translator
import writer

file_name = sys.argv[1]

def handle_bootstrap(asm_code):
    if not asm_code['is_dir']:
        return asm_code['lines']
    return   [
        '@256',
        'D=A',
        '@SP',
        'M=D'
    ] + asm_code['lines']

vm_code = get_lines.read_and_preprocess(file_name)
vm_code = tokanizer.tokanize(vm_code)
ass_code = translator.translate(vm_code)
ass_code['lines'] = handle_bootstrap(ass_code)
writer.write_to_asm_file(ass_code)
