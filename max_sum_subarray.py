#Max sum sub array
arr  = [2,-9,5,1,-4,6,0,-7,8]

#if all are negative return max of it
def max_sub_arr():
    
    k  = max(arr)
    if k<0:
        return k
    else:
        if arr ==[]:
            return 0
        else:
            current_sum = 0 
            max_sum = 0
            for val in arr:
                current_sum+=val
                if current_sum<0: 
                    current_sum = 0  #reset 

                elif current_sum>max_sum:
                    max_sum = current_sum
        return max_sum

                
max_sub_arr()
