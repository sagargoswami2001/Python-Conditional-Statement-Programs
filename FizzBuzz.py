''' Write a Python program which iterates the integers from 1 to 50. for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". for numbers which are multiples of both three and five print "FizzBuzz". '''
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
    