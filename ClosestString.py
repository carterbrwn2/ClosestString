# Author: Carter Brown

# Finds the geometrical "center" of input strings.
# Input contains the first line n, followed by n number of strings.

"""
EXAMPLE INPUT:

11
AACACCCTATA
CTTCATCCACA
TTTCAATTTTC
ACAATCAAACC
ATTCTACAACT
ATTCCTTATTC
ACTTCTCTATT
TAAAACTCACC
CTTTTCCCACC
ACCTTTTCTCA
TACCACTACTT

OUTPUT:
ATTCTACAACT

"""

# Read input

n = int(input())

strings = []

for i in range(n):
    strings.append(input())

# Create dict of lines and their distances

dist_map = {}
for i in range(n):
    seq = strings[i]
    distance_sum = 0
    for j in range(n):
        if i != j:
            comp = strings[j]
            for x in range(len(seq)):
                if seq[x] != comp[x]:
                    distance_sum += 1
    dist_map[seq] = distance_sum

# Print closest string

print(min(dist_map, key=dist_map.get))
