def count_numbers(sorted_list, less_than):
    
    if less_than <= sorted_list[0]: 
        return 0
    
    if less_than > sorted_list[-1]: 
        return len(sorted_list)
    
    ans = 0
    l, h = 0, len(sorted_list)-1 
    while l <= h:
        c = (l+h)//2
        
        if sorted_list[c] < less_than:
            ans = c + 1 
            l = c + 1
        else: 
            h = c - 1
         
    return ans    

if __name__ == "__main__":

    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2