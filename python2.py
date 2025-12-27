# Problem‑2: Generate a series of odd numbers up to n
a = int(input("Enter an ineger value for a: "))
series = [2 * i + 1 for i in range(a)]

print(",".join(map(str, series)))

# output
# Enter an ineger value for a: 4
# 1,3,5,7