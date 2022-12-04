def RabinKarp(sequence, pattern, d=4, q=10): #d - number of letter in alphabet, q - constant to work out overload problem
    n = len(sequence)
    m = len(pattern)
    pattern_hash = 0
    sequence_hash = 0
    indeces = [] # an output will be in a format of a list of starting index for pattern in sequence if such exists
    for i in range(len(pattern)): # let's determine an initial hash of our sequence and a hash of our pattern
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        sequence_hash = (d * sequence_hash + ord(sequence[i])) % q
    for i in range(n-m+1): # let's now find our pattern
        if pattern_hash == sequence_hash:
            if pattern == sequence[i:i+m]: # double check, because it might be a collision
                indeces.append(i)
        if i < n - m:
            sequence_hash = (d * (sequence_hash - ord(sequence[i]) * d**(m - 1) % q) + ord(sequence[i+m])) % q
    return indeces


seq = 'GCACTCAACT'
pat = 'ACT'
print(RabinKarp(seq, pat, 4, 10))
