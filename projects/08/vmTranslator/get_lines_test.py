import unittest
import get_lines 
import test_resources.BasicLoop.BasicLoopLineOutput as basicLoopLines
import test_resources.FibonacciElement.FibonacciLineOutput as fibLines

path_to_fib_dir = 'test_resources/FibonacciElement'
path_to_BasicLoop_vm_file = 'test_resources/BasicLoop/BasicLoop.vm'


class TestGetLines(unittest.TestCase):
    
    def test_format_line(self):
        line = "   POP TEST 4 //   \t\t\n"
        correct_format = "POP TEST 4"
        formatted_line = get_lines.format_line(line)
        self.assertEqual(formatted_line, correct_format)


    def test_get_lines_from_file(self):
        self.maxDiff
        result = get_lines.read_and_preprocess(path_to_BasicLoop_vm_file)
        self.assertEqual(result['lines'], basicLoopLines.lines)

    def test_get_lines_from_files(self):
        self.maxDiff
        result = get_lines.read_and_preprocess(path_to_fib_dir)
        self.assertEqual(result['lines'], fibLines.lines)


