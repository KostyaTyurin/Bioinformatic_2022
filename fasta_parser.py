"""Make sequence from fasta file"""


def read_fasta(filename=None):
    if filename is None:
        sequence = None
    else:
        import re

        f = open(filename, 'r')
        lines = f.readlines()

        hre = re.compile('>(\S+)')  # regular expression - used in searching for id
        lre = re.compile('^(\S+)$')  # regular expression - used in searching for DNA sequence

        gene = {}

        for line in lines:
            outh = hre.search(line)
            if outh:
                id = outh.group(1)
            else:
                outl = lre.search(line)
                if id in gene.keys():
                    gene[id] += outl.group(1)
                else:
                    gene[id] = outl.group(1)
        sequence = gene[id]
    return sequence
