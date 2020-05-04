import sys
import re
path_vcf = sys.arg[1]
path_ref = sys.arg[2]
reference = {}
vcf_dict = {}
reference_joined = {}
good_chrs = ['chr01', 'chr02', 'chr03', 'chr04', 'chr05', 'chr06']
bad_chrs = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6']



with open(path_vcf, 'r') as vcf:
    with open(path_ref, 'r') as ref:
        for v in vcf:
            v = v.strip()
            if v[0:3:1] == 'chr':
                v = v.split()
                vcf_dict.setdefault(str(v[0]), [])
                vcf_dict[str(v[0])].append([v[1], v[3], v[4]])
        for s in ref:
            s = s.strip()
            if (s[0] == '>') and s not in reference.keys():
                reference[s[1::]] = []
                tmp = s[1::]
            else:
                reference[tmp].append(s)


for k in reference.keys():

    if k in bad_chrs:
        g = good_chrs[bad_chrs.index(k)]
        reference_joined[g] = ''.join(reference[k])
    else:
        reference_joined[k] = ''.join(reference[k])

#print(reference[1])
for k in vcf_dict.keys():
    for l in range(len(vcf_dict[k])):
        pos = vcf_dict[k][l][0]
        length = len(vcf_dict[k][l][1])
        ref = reference_joined[k][int(vcf_dict[k][l][0]) - 1 - 15: int(vcf_dict[k][l][0]) - 1 + 15]

        for p in re.finditer(r'(?=(([ATGC]{2,15}))\1)', ref):
            if (p.start() + len(p[1]) + len(p[2])) >= 15:
                ref_rep = True
            else:
                continue
        alt = reference_joined[k][int(pos) - 1 - 15: int(pos) - 1] + vcf_dict[k][l][2] + reference_joined[k][int(pos) + length: int(pos) - 1 + 15]
        for o in re.finditer(r'(?=(([ATGC]{2,15}))\1)', alt):
            if (o.start() + len(o[1]) + len(o[2])) >= 15:
                alt_rep = True
            else:
                continue
        if alt_rep == True and ref_rep == False:
            print(vcf_dict[k][l], 'New repeat')
        if alt_rep == False and ref_rep == True:
            print(vcf_dict[k][l], 'Broken repeat')
        alt_rep = False
        ref_rep = False


    #print (vcf_dict[k], '\t', reference_joined[k][int(vcf_dict[k][0]) - 1])

