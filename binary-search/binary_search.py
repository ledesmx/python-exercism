def find(search_list, value):
    low = 0
    high = len(search_list)
    
    while low < high:
        print(low)
        print(high)
        needle = (low + high) // 2
        if search_list[needle] == value:
            return needle
        if search_list[needle] > value:
            high = needle
        else:
            low = needle + 1
    
    raise ValueError("value not in array")
