# Write a Python Program to Count the Number of Even and Odd Numbers from a Series of Numbers.
number = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the Tuple
count_odd = 0
count_even = 0
for x in number:
    if not x % 2:
        count_even+=1
    else:
        count_odd+=1
print("Number of Even Numbers: ", count_even)
print("Number of Odd Numbers: ", count_odd)
