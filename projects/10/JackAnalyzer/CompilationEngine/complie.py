


keyword_handlers = {
    'class': class_handler,
    'static': classVarDec_handler,
    'field': classVarDec_handler,
    '{': subroutineDec_handler
}

def handle_type_xml(type):
    if type in ['int', 'char', 'boolean']:
        return [
            "keyword>",
                type,
            "</keyword>",
        ]
    else:
        return [
             "<identifier>",
                type,
            "</identifier>",
        ]


def classVarDec_handler(tknizr):
    field_type = tknizr.getTokenValue()
    data_type = tknizr.next()
    result = [
        '<classVarDec>',
            '<keyword>',
                field_type,
            '</keyword>',
    ] + handle_type_xml(data_type.getTokenValue())

    data_type = tknizr.next()
    while (tknizr.getTokenValue() != ';'):
        current_token = tknizr.getTokenValue()
    
    
    result.append('</classVarDec>')
    return result

def class_handler(tknizr):
    name = tknizr.next().getTokenValue()
    tknizr.next().getTokenValue() #skip { 
    result = [ 
        '<class>', 
        '<keyword>', 
            'class', 
        '</keyword>', 
        '<identifier',
        name,
        '</identifier>',
        '<symbol>', 
        '{', 
        '</symbol>']
    
    while {tknizr.get_next_token_value() != '}'}:
        next_token = tknizr.next()
        block = keyword_handlers(next_token.getTokenValue())
        result = result + block
    
    tknizr.next().getTokenValue() #skip }

    result = result + [
         '<symbol>', 
        '}', 
        '</symbol>'
    ]
    result.append('</class>')
    return result


for file in jack_files:
    cur_tokenizer = file['Tokenizer']
    while (cur_tokenizer.hasMoreTokens()):
        cur_token = cur_tokenizer.next()
        token_type = cur_token.getTokenType()
        token_value = cur_token.getTokenValue();

        