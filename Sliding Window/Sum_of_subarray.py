def sum_subArray(num,k):
    n = len(num)
    if n < k:
        return -1
    
    cur_sum = sum(num[:k])
    max_sum = cur_sum

    for i in range(k,n):
        cur_sum += num[i] - num[i-k]
        max_sum = max(max_sum,cur_sum)
    
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(sum_subArray(arr,k))
