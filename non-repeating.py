my_char = dict()
string = "ADBCGHIEFKJLADTVDERFSWVGHQWCNOPENSMSJWIERTFB"
for alpha in string:
    my_char[alpha] = 0
for alpha in string:
    my_char[alpha] +=1
for alpha in string:
    if my_char[alpha]==1:
        print alpha
        break
