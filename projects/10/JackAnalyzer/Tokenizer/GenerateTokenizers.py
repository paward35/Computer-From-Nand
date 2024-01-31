import sys
import get_lines
from Tokenizer import Tokenizer 
import writer



KEY_WORDS = ['CLASS', 'METHOD', 'FUNCTION', 'CONSTRUCTOR', 'INT', 'BOOLEAN', 'CHAR', 'VOID', 'VAR', 'STATIC', 'FIELD', 'LET', 'DO', 'IF', 'ELSE', 'WHILE', 'RETURN', 'TRUE', 'FALSE', 'NULL', 'THIS']
SYMBOLS = "()[]{},;=.+-*/&|~<>"


def resolve_token_types(files):
    for file in files:
        labeled_tokens = []
        for token in file['tokens']:
            labeled_tokens.append(get_token_type(token))
        file['labeled_tokens'] = labeled_tokens


def replace_symbols_with_representation(token):
    token = token.replace('<', '&lt;')
    token = token.replace('>', '&gt;')
    token = token.replace('"', '&quot;')
    token = token.replace('&', '&amp;')
    return token


def get_token_type(token):
    if token in SYMBOLS:
        token = replace_symbols_with_representation(token)
        return f"<symbol>{token}</symbol>"
    elif token.upper() in KEY_WORDS:
        return f"<keyword>{token}</keyword>"
    elif token.isdigit():
        return f"<integerConstant>{token}</integerConstant>"
    elif token.startswith('"'):
        return f"<stringConstant>{token}</stringConstant>"
    else:
        return f"<identifier>{token}</identifier>"


def generate_tokenizers(path):
    file_name = sys.argv[1] if len(sys.argv) > 1 else ''
    jack_files = get_lines.read_and_preprocess(file_name)
    resolve_token_types(jack_files)
    for file in jack_files:
        file['Tokenizer'] = Tokenizer(file['labeled_tokens'])


