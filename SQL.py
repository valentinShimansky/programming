import pymysql
import sys

def table_creation(c):
    with c.cursor() as cur:
        cur.execute('''create table if not exists sequences (id int, DNA text, RNA text, Protein text, DNA_weight float, Protein_weight float)''')
        c.commit()

def db_insert(list, c):
    with c.cursor() as cur:
        cur.execute('''INSERT INTO sequences (id, DNA, RNA, Protein, DNA_weight, Protein_weight) VALUES (%s, %s, %s, %s, %s, %s)''', list)
        c.commit()

def reverse_complement(seq):
    reverse_dict = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A', }
    complement = ''
    for i in seq:
        complement += reverse_dict[i]
    return complement[len(complement):0:-1]


def triples_split(seq, reverse):
    result = []
    temp = []
    for i in range(0, 3):
        for j in range(0, len(seq), 3):
            temp.append(seq[j + i:j + i + 3:])
        result.append(temp)
    temp = []
    for i in range(0, 3):
        for j in range(0, len(seq), 3):
            temp.append(reverse[j + i:j + i + 3:])
        result.append(temp)
    return result


def orf_search(trip):
    result = []
    final_list = []
    res = ''
    for i in range(len(trip)):
        for j in range(len(trip[i])):
            if trip[i][j] == 'ATG':
                start = j
                for k in range(j, len(trip[i])):
                    if trip[i][k] in ['TAG', 'TGA', 'TAA']:
                        stop = k
                        for l in range(start, stop + 1):
                            res += trip[i][l]
                        break
                result.append(res)
                res = ''
    for m in range(len(result)):
        if (len(result[m]) / 3 >= 100) and (len(result[m]) % 3 == 0):
            final_list.append(result[m])
    return (final_list)


def transcription(seq):
    rna_seq = ''
    RNA_dict = {'A': 'A', 'G': 'G', 'C': 'C', 'T': 'U', }
    for i in seq:
        rna_seq += RNA_dict[i]
    return rna_seq


def translation(seq):
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
    for i in range(0, len(seq), 3):
        prot += AA[seq[0 + i:3 + i:]]
    return prot


def weight_count(prot):
    weights = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
               'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
               'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
               'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06}
    prot_weight = 0

    for j in prot:
        if j != '_':
            prot_weight += weights[j]
    return prot_weight


conn = pymysql.connect('localhost', 'root', 'genesis123', 'orfs')
table_creation(conn)


posl = sys.stdin

# with open('C:\\Users\\Win10Pro\\Desktop\\python\\input.txt', 'r') as inf:
#     for s in inf:
#         s = s.strip()
#         posl += s

posl_rev = reverse_complement(posl)
triples = triples_split(posl, posl_rev)
orfs = orf_search(triples)
orf_weight = []
orf_rna = []
orf_protein = []
orf_prot_weight = []

for z in range(len(orfs)):
    orf_weight.append(len(orfs[z]) * 345 / 1000)
    orf_rna.append(transcription(orfs[z]))
    orf_protein.append(translation(orfs[z]))
    orf_prot_weight.append(weight_count(orfs[z]))
    tmp = [z, orfs[z], orf_rna[z], orf_protein[z], orf_weight[z], orf_prot_weight[z]]
    db_insert(tmp, conn)

