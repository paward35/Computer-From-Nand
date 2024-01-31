

def write_to_asm_file(code):
    with open(code['result_file'], "w") as outfile:
        outfile.write("\n".join(code['lines']))