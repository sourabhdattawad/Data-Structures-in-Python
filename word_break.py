#Word break problem


#Recursion (prefix+suffix)
arr = ['I','AM','SOURABH']
string = 'IAMSOURABH'

def word_break(st):
    n = len(st)
    if n==0:
        return True
    for i in range(1,n+1):
        if st[0:i] in arr and word_break(st[i:n]):
            print st[0:i]
            return True
    return False
print word_break(string)

#DP solution
bool_array = [False for i in range(len(string)+1)]

def dp_wordbreak():
    
    n = len(string)
    for i in range(1,n+1):
        if string[0:i] in arr:
            bool_array[i]=True

        if bool_array[i]==True and i==(n-1):
            return True

        if bool_array[i]==True:
            for j in range(i, n+1):
                if bool_array[j]==True and j==(n-1):
                    return True
                if string[i:j] in arr:
                    bool_array[j] = True
    return bool_array[-1]
print dp_wordbreak()


# string = 'ILOVEPYTHON'
# array = ['I','LOVE','PYTHON','JAVA']
# bool_array = [False for i in range(len(string))]
# for i in range(0, len(string)):
#     k  = string[:i+1]
#     if k in array:
#         bool_array[i] = True
#     if bool_array[i] == True:
#         for j in range(i+1, len(string)):
#             k  = string[i+1:j+1]
#             if k in array:
#                 bool_array[j]= True

# print bool_array[-1]
# if bool_array[-1]:
#     new_string = ""
#     for i in range(len(string)):
#         if bool_array[i]==True:
#             new_string+=string[i]+' '
#         else:
#             new_string+=string[i]
#     print new_string
    
            
            


                
        
        
        

