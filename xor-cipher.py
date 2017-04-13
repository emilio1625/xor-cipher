#!/usr/bin/env python3
# Copyright (C) 2017 Emilio Cabrera
"""xor-cipher

Small and simple xor cipher script
"""
import argparse
from os import path

parser = argparse.ArgumentParser(description='Simple XOR encryption and '
                                             'decryption script')
parser.add_argument('-t', '--text', help='text to encrypt/decrypt')
parser.add_argument('-f', '--file', help='plain text file to encrypt/decrypt')
parser.add_argument('-k', '--key', help='key for encryption')
parser.add_argument('-K', '--key-file', help='plain text file containing the '
                                             'key for encryption/decryption')
parser.add_argument('-o', '--output', help='file to output encrypted text')
parser.add_argument('-r', '--raw', action='store_true', default=False,
                    help='prints raw text i.e. showing escape caracters')


def read_multiline():
    lines = []
    while True:
        line = input("")
        if line:
            lines.append(line)
        else:
            break
    return tuple(lines)


def xor_cipher(text, keys):
    result = []
    i = 0
    j = 0
    for line in text:
        cline = ""
        for char in line:
            if i == len(keys[j]):
                j = j + 1 if j < len(keys) else 0
                i = 0
            cline += chr(ord(char) ^ ord(keys[j][i]))
        result.append(cline)
    return tuple(result)


def main():
    args = parser.parse_args()

    if not args.text:
        if not args.file:
            print('Please write the text to encrypt/decrypt (empty line to '
                  'finish):')
            text = read_multiline()
        else:
            print('Reading file to encrypt/decrypt')
            fin = args.file
            while not path.isfile(fin):
                print("File doesn't exits, enter path again:")
                fin = input()
            file = open(fin, 'r')
            text = file.readlines()
            file.close()
    else:
        text = tuple(args.text)

    if not args.key:
        if not args.key_file:
            key = input('Please write the key for encrypt/decrypt: ')
        else:
            print('Reading key file')
            fin = args.key_file
            while not path.isfile(fin):
                print("File doesn't exits, enter path again:")
                fin = input()
            file = open(args.key_file, 'r')
            key = file.readlines()
            file.close()
    else:
        key = tuple(args.key)

    result = xor_cipher(text, key)

    if args.output:
        fout = args.output
        mode = 'x'
        while path.isfile(fout):
            if path.isfile(fout):
                opt = input("File exits, overwrite? (Y/n): ")
                if opt.lower() == 'y':
                    mode = 'w'
                    break
                else:
                    fout = ''
                    while not fout:
                        fout = input("Enter filename for output: ")
        f = open(fout, mode)
        f.writelines(result)
        f.close()
    elif args.raw:
        print('\nResult:\n')
        print(result)
    else:
        print('\nResult:\n')
        for line in result:
            print(line)


if __name__ == '__main__':
    main()
