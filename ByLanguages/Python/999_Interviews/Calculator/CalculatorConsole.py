"""
@Author: Rahul Vats
@AuthorEmail: vats.rahul@gmail.com
@Note: This is a console based calculator program
"""
''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''


# This function adds two numbers
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y


# This function divides two numbers11
def divide(x, y):
   return x / y

# This function calculate modulus of x with y
def modulus(x, y):
   return x % y 

# This function calculate power of x with y
def power(x, y):
   return x ** y


# This function calculate floordivision of x with y
def floordivision(x, y):
   return x // y

# This function shifts y bits in x to left
def leftshift(x, y):
   return x << y

# This function shifts y bits in x to right
def rightshift(x, y):
   return x >> y

# This function performs bitwise and operation or Sets each bit to 1 if both bits are 1 on bits of x and y
def andoperator(x, y):
   return x & y

# This function performs bitwise or operation or Sets each bit to 1 if either bits are 1 on bits of x and y
def oroperator(x, y):
   return x | y

"""
Python's Binary Operator
   Python's Arithmetic Operator
+	Addition	        x + y	
-	Subtraction	        x - y	
*	Multiplication	        x * y	
/	Division	        x / y	
%	Modulus	                x % y	
**	Exponentiation	        x ** y	 
//	Floor division	        x // y
   Python Bitwise Operators
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
 ^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
Python's Unary Operator
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
"""

print("Select any operation listed below.")
print("1. Add or +")
print("2. Subtract or -")
print("3. Multiply or *")
print("4. Divide or /")
print("5. Modulus or %")
print("6. Power or **")
print("7. Floor division or //")
print("8. Left Shift or <<")
print("9. Right Shift or >>")
print("10. AND or &")
print("11. OR or |")
choice = "Y"
while (choice != "N"):
    # Take input from the user
    choice = input("Enter choice [(either 1 or 2 or ... or 11) or (operator sign as +, -, *, ^, /, etc)]: ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1' or choice == '+':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2' or choice == '-':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3' or choice == '*':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4' or choice == '/':
        if num2 == 0:
            print("Division by 0 is ∞")
        else:
            print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == '5' or choice == '%':
        print(num1, "%", num2, "=", modulus(num1, num2))

    elif choice == '6' or choice == '**':
        print(num1, "**", num2, "=", power(num1, num2))

    elif choice == '7' or choice == '//':
        print(num1, "//", num2, "=", floordivision(num1, num2))

    elif choice == '8' or choice == '<<':
        print(num1, "<<", num2, "=", leftshift(num1, num2))

    elif choice == '9' or choice == '>>':
        print(num1, ">>", num2, "=", rightshift(num1, num2))

    elif choice == '10' or choice == '&':
        print(num1, "&", num2, "=", andoperator(num1, num2))

    elif choice == '11' or choice == '|':
        print(num1, "|", num2, "=", oroperator(num1, num2))

    elif choice == 'N':
        continue

    else:
        print("Invalid input")
