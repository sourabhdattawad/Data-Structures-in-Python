#shortest palindrome
#Take substrings from i to n-1, reverse and add to string check for palindrome 
a = 'abcd'
for i in range(len(a)+1):
    k =a[:i]
    temp =  a+k[::-1] 
    print temp, temp[::-1]
    if temp ==temp[::-1]:
        print temp
        break
