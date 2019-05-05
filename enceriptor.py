import argparse
import sys
import string
import collections
import time
import sys

alf = string.ascii_lowercase * 10 + string.ascii_uppercase * 10
lowercase_set = set(string.ascii_lowercase)
alf_set = set(string.ascii_letters)


def find(code, symbol):
    if code == 'encode':
        return alf.find(symbol)
    elif code == 'decode':
        return len(string.ascii_lowercase) - alf.find(symbol)
    else:
        print('bad code')
        raise NameError


def read(file):
    if file == 'sys.stdin':
        return input()
    else:
        with open(file, 'r') as f:
            return f.read()


def write(file, res):
    if file == 'sys.stdout':
        print(res)
    else:
        with open(file, 'w') as f:
            f.write(res)


def give_caesar(code, str1, key):
    res = []
    for i in range(len(str1)):
        if alf.find(str1[i]) != -1:
            res.append((alf[alf.find(str1[i]) + find(code, alf[key])]))
        else:
            res.append(str1[i])
    return ''.join(map(str, res))


def give_vigenere(code, str1, key1):
    res = []
    for i in range(len(str1)):
        if alf.find(str1[i]) != -1 and find('encode', key1[i]) != -1:
            res.append(alf[alf.find(str1[i]) + find(code, key1[i])])
        else:
            res.append(str1[i])
    return ''.join(map(str, res))


def caesar(code, args):
    res = give_caesar(code, read(args.input_file), int(args.key))
    write(args.output_file, res)


def vigenere(code, args):
    str1 = read(args.input_file)
    attitude = (len(str1) + len(args.key)) // len(args.key)
    key1 = args.key * attitude
    write(args.output_file, give_vigenere(code, str1, key1))


def encode(args):
    if args.cipher == 'caesar':
        caesar('encode', args)
    elif args.cipher == 'vigenere':
        vigenere('encode', args)
    else:
        raise NameError


def decode(args):
    if args.cipher == 'caesar':
        caesar('decode', args)
    elif args.cipher == 'vigenere':
        vigenere('decode', args)
    else:
        raise NameError
