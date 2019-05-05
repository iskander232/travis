from  pytest import *
from enceriptor import *
from for_test import *

def test_caesar():
   args = C('files/text1', 'files/out1', 17)
   caesar('encode', args)
   assert read('files/text1') == give_caesar('decode', read('files/out1'), 17)


def test_viginere():
    args = C('files/text1', 'files/out2_1', 'files/text2')
    vigenere('encode', args)
    args.input_file = 'files/out2_1'
    args.output_file = 'files/out2_2'
    vigenere('decode', args)
    assert read('files/out2_2') == read('files/text1')

