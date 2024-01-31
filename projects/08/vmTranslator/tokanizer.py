
def tokanize(code):
    for line in code['lines']:
        line['code'] = line['code'].split(' ')
    return code
