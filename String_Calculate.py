# Write a Python program that accepts a string and calculate the number of digits and letters.
s = input("Input a String: ")
d = l = 0
for c in s:
    if c.isdigit():
        d = d+1
    elif c.isalpha():
        l= l+1
    else:
        pass
print("Letters", l)
print("Digits", d)
