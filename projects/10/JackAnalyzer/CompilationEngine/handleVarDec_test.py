import unittest
from handlers import handle_controller
import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from Tokenizer.TokenizerProvider import Tokenizer 

class TestVarDecHandler(unittest.TestCase):

    def test_classVarDec_static(self):
        input = [
            '<keyword>static</keyword>',
            '<keyword>boolean</keyword>',
            '<identifier>test</identifier>',
            '<symbol>;</symbol>'
        ]
        tknizer = Tokenizer(input)
        next(tknizer)
        output = handle_controller(tknizer)
        expected_output = [
            '<classVarDec>',
                '<keyword>static</keyword>',
                '<keyword>boolean</keyword>',
                '<identifier>test</identifier>',
                '<symbol>;</symbol>',
            '</classVarDec>'
        ]

        self.assertEqual(output, expected_output)

    def test_classVarDec_field(self):
        input = [
            '<keyword>field</keyword>',
            '<keyword>boolean</keyword>',
            '<identifier>test</identifier>',
            '<symbol>;</symbol>'
        ]
        tknizer = Tokenizer(input)
        next(tknizer)
        output = handle_controller(tknizer)
        expected_output = [
            '<classVarDec>',
                '<keyword>field</keyword>',
                '<keyword>boolean</keyword>',
                '<identifier>test</identifier>',
                '<symbol>;</symbol>',
            '</classVarDec>'
        ]

        self.assertEqual(output, expected_output)


    def test_classVarDec_className(self):
        input = [
            '<keyword>field</keyword>',
            '<identifier>myClass</identifier>',
            '<identifier>test</identifier>',
            '<symbol>;</symbol>'
        ]
        tknizer = Tokenizer(input)
        next(tknizer)
        output = handle_controller(tknizer)
        expected_output = [
            '<classVarDec>',
                '<keyword>field</keyword>',
                '<identifier>myClass</identifier>',
                '<identifier>test</identifier>',
                '<symbol>;</symbol>',
            '</classVarDec>'
        ]

        self.assertEqual(output, expected_output)


    def test_classVarDec_multiple_vars(self):
        input = [
            '<keyword>field</keyword>',
            '<keyword>int</keyword>',
            '<identifier>x</identifier>',
            '<symbol>,</symbol>',
            '<identifier>y</identifier>',
            '<symbol>;</symbol>',
        ]
        tknizer = Tokenizer(input)
        next(tknizer)
        output = handle_controller(tknizer)
        expected_output = [
            '<classVarDec>',
            '<keyword>field</keyword>',
            '<keyword>int</keyword>',
            '<identifier>x</identifier>',
            '<symbol>,</symbol>',
            '<identifier>y</identifier>',
            '<symbol>;</symbol>',
            '</classVarDec>'
        ]

        self.assertEqual(output, expected_output)

    def test_VarDec_multiple_vars(self):
        input = [
            '<keyword>var</keyword>',
            '<keyword>int</keyword>',
            '<identifier>x</identifier>',
            '<symbol>,</symbol>',
            '<identifier>y</identifier>',
            '<symbol>;</symbol>',
        ]
        tknizer = Tokenizer(input)
        next(tknizer)
        output = handle_controller(tknizer)
        expected_output = [
            '<varDec>',
            '<keyword>var</keyword>',
            '<keyword>int</keyword>',
            '<identifier>x</identifier>',
            '<symbol>,</symbol>',
            '<identifier>y</identifier>',
            '<symbol>;</symbol>',
            '</varDec>'
        ]

        self.assertEqual(output, expected_output)
