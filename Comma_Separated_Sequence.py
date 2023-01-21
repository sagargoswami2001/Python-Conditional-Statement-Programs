# Write a Python Program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. the numbers obtained should be printed in a comma-separated sequence.
items = []
for i in range(100, 401):
    s = str(i)
    if (int (s[0]) % 2 == 0) and (int (s[1]) % 2 == 0) and (int (s[2]) % 2 == 0):
        items.append(s)
print(",".join(items))
