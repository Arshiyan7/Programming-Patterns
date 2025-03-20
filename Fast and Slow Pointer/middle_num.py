def is_happy(n):
    def next_number(n):
        return sum(int(digit) ** 2 for digit in str(n))  
    
    slow = n
    fast = next_number(n)  
    
  
    while fast != 1 and slow != fast:
        slow = next_number(slow) 
        fast = next_number(next_number(fast)) 
    
    
    if fast == 1:
        return -1  

    
    cycle_numbers = []
    slow = next_number(slow) 
    cycle_numbers.append(slow)

    while True:
        slow = next_number(slow)
        if slow in cycle_numbers:
            break
        cycle_numbers.append(slow)

    return cycle_numbers[len(cycle_numbers) // 2]

print(is_happy(85))
