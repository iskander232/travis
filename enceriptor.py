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


def model_to_statistic(file):
    """
    This function returns symbol statistics by modul file
    :param file:
    :return:
    """
    d = dict()
    with open(file, 'r') as f:
        for i in range(len(string.ascii_letters)):
            line = f.readline()
            d[string.ascii_letters[i]] = float(line[:-1])
    return d


def statistic(s):
    d = collections.Counter((ch for ch in s if ch in alf_set))
    sum1 = 0
    for i in alf:
        sum1 += d[i]
    for i in string.ascii_letters:
        d[i] /= sum1
    return d


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


def train(args):
    d = statistic(read(args.input_file))
    res = []
    for i in string.ascii_letters:
        res.append(str(d[i]))
        res.append("\n")
    write(args.model_file, ''.join(map(str, res)))


def hack(args):
    s = read(args.input_file)
    local_min = float("inf")
    d = model_to_statistic(args.model_file)
    res = ''
    s1 = give_caesar('decode', s, 0)
    d1 = statistic(s1)
    for i in string.ascii_lowercase:
        dist = 0
        for c in string.ascii_letters:
            dist += abs(d[alf[alf.find(i) + alf.find(c)]] - d1[c])
        if dist < local_min:
            local_min = dist
            res = i
    write(args.output_file, give_caesar('encode', s1, string.ascii_lowercase.find(res)))
