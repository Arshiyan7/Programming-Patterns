def sum_of_K(array, k):
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] + array[right] == k:
            return [left + 1, right + 1]  

        elif array[left] + array[right] < k:
            left += 1  

        else:
            right -= 1  

    return []  

n = [1, 4, 5, 7, 8]
v = 6
print(sum_of_K(n, v))
