from  pytest import *
from enceriptor import *
from for_test import *

def test_caesar():
   args = C('text1', 'out1', 17)
   caesar('encode', args)
   assert read('text1') == give_caesar('decode', read('out1'), 17)


def test_viginere():
    args = C('text1', 'out2_1', 'text2')
    vigenere('encode', args)
    args.input_file = 'out2_1'
    args.output_file = 'out2_2'
    vigenere('decode', args)
    assert read('out2_2') == read('text1')

