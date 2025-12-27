# Problem‑3: Generate a series of odd numbers up to n (inclusive if n is odd) 
a = int(input("Enter an integer a:"))

if a % 2 == 0:
    a -= 1 
series = [ 2 * i + 1 for i in range(a)]

print(",".join(map(str, series)))

# output 

# Enter an integer a:6
# 1,3,5,7,9