# Write a Python Program that Accepts a Word from the User and Reverse it.
word = input("Input a Word to Reverse: ")
for char in range(len(word) -1, -1, -1):
    print(word[char], end="")
print('\n')
