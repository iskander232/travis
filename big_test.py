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


def test_hack():
    args_train = C('text1', None, None, 'model_1')
    train(args_train)
    args_encode = C('war_and_piece', 'out3', 25)
    caesar('encode', args_encode)
    args_hack = C('out3', 'out4', None, 'model_1')
    hack(args_hack)
    assert read('war_and_piece') == read('out4')
