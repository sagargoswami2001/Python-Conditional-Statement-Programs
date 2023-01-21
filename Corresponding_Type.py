# Write a Python Program that prints each item and its corresponding type from the following list.

datalist = [2706, 27.00, 1+2j, True, 'Sagar', (27, 2001), [27, 2001], {"Course":'BCA', "Section":'A'}]
for item in datalist:
    print("Type of ", item, " is ", type(item))
    