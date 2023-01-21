# Write a Python Program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

n1 = []
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        n1.append(str(x))
print(','.join(n1))
