dict1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
roman = "MCMIV"
res = 0
for i in range(len(roman)-1):
    if dict1[roman[i]]>=dict1[roman[i+1]]:
        res+= dict1[roman[i]]
    else:
        res-= dict1[roman[i]]
print res+dict1[roman[-1]]
