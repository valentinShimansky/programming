import sys
def medium_count(k, s):
    summ = 0
    current_start = 0
    for i in range(s.count(k)):
        summ += s.find(k, current_start)
        current_start = s.find(k, current_start) + 1
    result = summ / s.count(k)
    return result


kmers_length = sys.stdin

sequence = input()
known_kmers = []
print ('KMER', '\t', 'START', '\t', 'FINISH', '\t', 'AVG')
for i in range(0, len(sequence) - kmers_length):
    kmer = sequence[i:i + kmers_length:]
    if kmer not in known_kmers:
        print(kmer, '\t', sequence.find(kmer), '\t', sequence.rfind(kmer), '\t', medium_count(kmer, sequence))
    else:
        continue