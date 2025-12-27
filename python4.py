# Problem‑4: Count numbers divisible by integers 1 to 9 in a given list
 
nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

result =  {}
for i in range(1, 10):
    count = sum(1 for n in nums if n % i == 0)
    result[i] = count
print(result)

# output

# {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
