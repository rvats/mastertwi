"""
@Author: Rahul Vats
@AuthorEmail: vats.rahul@gmail.com
@Note: This program shows string literals and some of their operations
"""
stringLiteral = "Hello"
for i in range(5):
    print("Character at ", i, " position in String Literal ", stringLiteral, " is ", stringLiteral[i])

stringLiteral = "Universe!"
for i in range(9):
    print(stringLiteral[0:i])

stringLiteral = " Hello, Universe! "
print("Length of ",stringLiteral," is ",len(stringLiteral),"Length of ",stringLiteral.strip(),"' is ",len(stringLiteral.strip()))
