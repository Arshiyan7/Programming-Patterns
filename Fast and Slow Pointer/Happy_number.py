def is_happy(n):
    def next_number(n):
        return sum(int(digit) ** 2 for digit in str(n))  

    slow = n
    fast = next_number(n)  
    
    while fast != 1 and slow != fast:
        slow = next_number(slow) 
        fast = next_number(next_number(fast)) 

    return fast == 1 

print(is_happy(19))