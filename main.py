"""Main file for run"""

import fasta_parser
import RabinKarp

try:
    text = input('Type the filename.fasta where text is: ')
    pattern = input('Type the filename.fasta where pattern is: ')

    text = fasta_parser.read_fasta(text)
    pattern = fasta_parser.read_fasta(pattern)
except FileNotFoundError:
    print('try again. no such file or directory')

text = RabinKarp.DNA(text)
pattern = RabinKarp.DNA(pattern)

try:
    print(RabinKarp.RabinKarp(text, pattern))
except IndexError:
    print('something is wrong with the sequence given. check that files are in FASTA format and try again')

