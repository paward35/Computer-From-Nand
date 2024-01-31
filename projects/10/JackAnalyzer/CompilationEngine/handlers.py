


def handler_varDec(tknizr):
    context = 'varDec' if tknizr.getTokenValue() == 'var' else 'classVarDec'
    result = [f'<{context}>']
    result.append(tknizr.getCurrentToken()) # field or static
    result.append(next(tknizr).getCurrentToken()) # type
    result.append(next(tknizr).getCurrentToken()) # name
    next_token = next(tknizr).getCurrentToken()
    while (';' not in next_token):
        result.append(next_token) # append ,
        result.append(next(tknizr).getCurrentToken()) # var name
        next_token = next(tknizr).getCurrentToken()
    result.append(next_token) # var name ;
    result.append(f'</{context}>')
    return result


def handler_expresion(tknizr):
    result = []
    return result


handle_map = {
    'static': handler_varDec,
    'field': handler_varDec,
    'var': handler_varDec
}

def handle_controller(tknizer):
    handler = handle_map[tknizer.getTokenValue()]
    return handler(tknizer)

