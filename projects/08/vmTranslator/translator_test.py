import unittest
import translator
import tokanizer 
import get_lines
import test_resources.BasicLoop.BasicLoopLineOutput as basicLoopLines
import test_resources.FibonacciElement.FibonacciLineOutput as fibLines

path_to_fib_dir = 'test_resources/FibonacciElement'
path_to_BasicLoop_vm_file = 'test_resources/BasicLoop/BasicLoop.vm'


class TestTranslator(unittest.TestCase):
    def test_translator(self):
        lines = get_lines.read_and_preprocess(path_to_BasicLoop_vm_file)
        processed_vm_code = tokanizer.tokanize(lines)
        ass_code = translator.translate(processed_vm_code)
        self.assertEqual(basicLoopLines.asm, ass_code)


