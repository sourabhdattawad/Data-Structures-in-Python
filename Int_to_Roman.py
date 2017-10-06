dict1 = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'L', 9:'IX', 5:'V', 4:'IV', 1:'I'}
array = [1000,900,400,500,100,90,50,40,10,9,5,4,1]
res = 1904
roman = ""
for i in range(len(array)):
    if res>=array[i]:
        res=res%array[i]
        roman+= dict1[array[i]]
print roman
