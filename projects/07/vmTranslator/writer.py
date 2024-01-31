import sys

def write_to_asm_file(input_file_name, code):
    file_name = input_file_name.split('.')[0]
    with open(f"{file_name}.asm", "w") as outfile:
        outfile.write("\n".join(code))