import sys

class DNA:

    def __init__(self, sequence):
        self.seq = sequence
        self.len = len(sequence)
        self.triples = []
        self.longest_orf = ''

    def triples_split(self):
        result = [[], [], []]
        temp = []
        for i in range(0, 3):
            for j in range(0, self.len, 3):
                temp.append(self.seq[j + i:j + i + 3:])
            result[i] = temp
        self.triples = result

    def orf_search(self):
        result = []
        res = ''
        longest_ORF = ''
        for i in range(len(self.triples)):
            for j in range(len(self.triples[i])):
                if self.triples[i][j] == 'ATG':
                    start = j
                    for k in range(j, len(self.triples[i])):
                        if self.triples[i][k] in ['TAG', 'TGA', 'TAA']:
                            stop = k
                            for l in range(start, stop + 1):
                                res += self.triples[i][l]
                            break
                    result.append(res)
                    res = ''
        for m in range(len(result)):
            tmp = result[m]
            if (len(tmp) >= 120) and (len(tmp) > len(longest_ORF)):
                longest_ORF = tmp
        self.longest_orf = longest_ORF
        print('longest ORF is:', longest_ORF)
        print('ORF DNA molecular weight:', (len(longest_ORF) * 345) / 1000, 'kD')


class RNA(DNA):

    def __init__(self, sequence):
        self.rna_seq = ''
        DNA.__init__(self, sequence)

    def transctiption(self):
        rna_seq = ''
        RNA_dict = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A', }

        for i in self.longest_orf:
            rna_seq += RNA_dict[i]
        self.rna_seq = rna_seq
        print('RNA sequence:', rna_seq)


class Protein(RNA):

    def __init__(self, sequence):
        RNA.__init__(self, sequence)

    def translation(self):
        prot = ''
        AA = {'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
                 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
                 'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
                 'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
                 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
                 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
                 'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
                 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
                 'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
                 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
                 'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
                 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
                 'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
                 'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
                 'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
                 'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
                 }
        weights = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
                   'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
                   'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
                   'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06}
        prot_weight = 0
        for i in range(0, len(self.longest_orf), 3):
            prot += AA[self.longest_orf[0 + i:3 + i:]]
        print('protein sequence:', prot)
        for j in prot:
            if j != '_':
                prot_weight += weights[j]
        print('protein weight:', prot_weight/1000, 'kD')
posl = sys.stdin

#with open('C:\\Users\\Win10Pro\\Desktop\\python\\input.txt', 'r') as inf:
#    for s in inf:
#        s = s.strip()
#        posl += s

test2 = Protein(posl)
test2.triples_split()
test2.orf_search()
test2.transctiption()
test2.translation()

