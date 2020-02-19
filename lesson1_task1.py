#convert from given to decim and addition
def decim (s1, n1, n2):
    dec1 = 0
    dec2 = 0
    for dig in range(len(n1)):
        if n1[dig] not in letter_number.keys():
            dec1 += int(n1[dig]) * (int(s1) ** abs(dig-len(n1) + 1))
        else:
            dec1 += int(letter_number[n1[dig]]) * (int(s1) ** abs(dig-len(n1) + 1))
    for dig2 in range(len(n2)):
        if n2[dig2] not in letter_number.keys():
            dec2 += int(n2[dig2]) * (int(s1) ** abs(dig2-len(n2) + 1))
        else:
            dec2 += int(letter_number[n2[dig2]]) * (int(s1) ** abs(dig2-len(n2) + 1))
    summ = dec1 + dec2
    return summ

#converting the result of sum
def final_convert (dec, s2):
    quot = dec
    result = ''
    while quot > s2:
        temp = quot % s2
        quot = quot // s2
        if temp > 9:
            result += get_key(letter_number, temp)
        else:
            result += str(temp)
    if quot > 9:
        result += get_key(letter_number, quot)
    else:
        result += str(quot)
    return result[len(result)::-1]

#function to search keys by value (C)stackoverflow
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
    
letter_number = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35} 
    
print('please enter 4 numbers divided by space')
inp = input().split()
sys1 = inp[0]
numb1 = list(inp[1])
numb2 = list(inp[2])
sys2 = int(inp[3])
print('result is: ', final_convert(decim(sys1, numb1, numb2), sys2))