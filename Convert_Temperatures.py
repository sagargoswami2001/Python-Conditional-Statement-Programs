# Write a Python Program to Convert Temperatures to and from Celsius, Fahrenheit.

# Formula: c = (5/9)*(F-32)
temp = input("Input the Temperature You Like to Convert? (Ex: 45F, 102C Etc.): ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"
else:
    print("Input Proper Convention.")
    quit()
print("The Temperature in", o_convention, "is", result, "Degrees.")
