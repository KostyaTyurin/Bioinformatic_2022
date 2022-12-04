class DNA:

    def __init__(self, filename = None):
        if filename != None:
            self.read_fasta(filename)
            self.length = len(self.sequence)
        else:
            self.sequence = None
            self.length = 0

    def read_fasta(self, filename):
        import re

        f = open(filename, 'r')
        lines = f.readlines()

        hre = re.compile('>(\S+)') # regular expression - used in searching for id
        lre = re.compile('^(\S+)$') # regular expression - used in searching for DNA sequence

        gene = {}

        for line in lines:
            outh = hre.search(line)
            if outh:
                id = outh.group(1)
            else:
                outl = lre.search(line)
                if (id in gene.keys()):
                    gene[id] += outl.group(1)
                else:
                    gene[id] = outl.group(1)
        self.sequence = gene[id]


def RabinKarp(text: DNA, pattern: DNA, d=4, q=10): #d - number of letter in alphabet, q - constant to work out overload problem
    n = text.length
    m = pattern.length
    pattern_hash = 0
    sequence_hash = 0
    indeces = [] # an output will be in a format of a list of starting index for pattern in sequence if such exists
    for i in range(m): # let's determine an initial hash of our sequence and a hash of our pattern
        pattern_hash = (d * pattern_hash + ord(pattern.sequence[i])) % q
        sequence_hash = (d * sequence_hash + ord(text.sequence[i])) % q
    for i in range(n-m+1): # let's now find our pattern
        if pattern_hash == sequence_hash:
            if pattern.sequence == text.sequence[i:i+m]: # double check, because it might be a collision
                indeces.append(i)
        if i < n - m:
            sequence_hash = (d * (sequence_hash - ord(text.sequence[i]) * d**(m - 1) % q) + ord(text.sequence[i+m])) % q
    for j in range(len(indeces)):
        print(text.sequence)
        print('-' * (indeces[j]), pattern.sequence, '-' * (n - m - indeces[j]), sep='')
    return indeces


if __name__=='__main__':
    text = DNA('dna_seq.fasta')
    pattern = DNA('pattern_seq.FASTA')
    RabinKarp(text, pattern)
