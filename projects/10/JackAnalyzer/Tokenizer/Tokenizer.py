import xml.etree.ElementTree as ET


class Tokenizer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None

    def __iter__(self):
        return self


    def __next__(self):
        if not self.hasMoreTokens():
            raise StopIteration
        self.current_token = self.tokens.pop(0)
        self.current_token_xml = ET.XML(self.current_token)
        return self


    def hasMoreTokens(self):
        return self.tokens


    def getTokenType(self):
        return self.current_token_xml.tag


    def getCurrentToken(self):
        return self.current_token


    def getTokenValue(self):
        return self.current_token_xml.text


    def get_next_token_value(self):
        next_token = self.tokens[1]
        next_token_xml = ET.XML(next_token)
        return next_token_xml.text

