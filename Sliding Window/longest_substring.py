def longest_substring(input_val):
    left = 0
    right = left 
    n = len(input_val) 
    max_str = 0
    unique_val = set()

    while right < n:
        if input_val[right] not in unique_val:
            unique_val.add(input_val[right])
            max_str = max(max_str, right - left + 1)
            right += 1
        
        else:
            unique_val.remove(input_val[left])
            left += 1

    return max_str

string = "abccabcbb"
print(longest_substring(string))  
