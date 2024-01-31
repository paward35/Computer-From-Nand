import sys
import get_lines
import tokanizer
import translator
import writer

file_name = sys.argv[1]

vm_code = get_lines.read_and_preprocess(file_name)
vm_code = tokanizer.tokanize(vm_code)
ass_code = translator.translate(file_name, vm_code)
writer.write_to_asm_file(file_name, ass_code)
