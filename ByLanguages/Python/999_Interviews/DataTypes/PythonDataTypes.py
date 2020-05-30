"""
@Author: Rahul Vats
@AuthorEmail: vats.rahul@gmail.com
@Note: This program illustrates the use of datatypes for variable
"""
# Declare a variable x as 5
x = 5
print("x = ",x,type(x))

# Declare y as John
y = "John"
print("y = ", y,type(y))

# Assign John in y to x which had 5
x = y
print("Assigning y to x")
print("x = ",x,type(x))

# Addign Float value 99.9 to y
y = 99.9
print("y = ", y,type(y))

# Assign 99.9 in y to x which had John
x = y
print("Assigning y to x")
print("x = ",x,type(x))
print("Python is awesomer than C, C++, C#, Java, etc.")

# Again manipulating types of variables
x = "Python is "
y = "awesome."
z =  x + y
print("x = ", x, " Type of x = ", type(x),"\n\t", "y = ", y, " Type of y = ", type(y), "\n\t", "z = ", z, " Type of z = ", type(z))

# Again manipulating types of variables
x = 5
y = 10
z =  x + y
print("x = ", x, " Type of x = ", type(x),"\n\t", "y = ", y, " Type of y = ", type(y), "\n\t", "z = ", z, " Type of z = ", type(z))

# Again manipulating types of variables
x = 1.5
y = 10
z =  x + y
print("x = ", x, " Type of x = ", type(x),"\n\t", "y = ", y, " Type of y = ", type(y), "\n\t", "z = ", z, " Type of z = ", type(z))

x = 1
y = 2.8
z = 1j
print("x = ", x, " Type of x = ", type(x),"\n\t", "y = ", y, " Type of y = ", type(y), "\n\t", "z = ", z, " Type of z = ", type(z))

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print("x = ", x, " Type of x = ", type(x),"\n\t", "y = ", y, " Type of y = ", type(y), "\n\t", "z = ", z, " Type of z = ", type(z))

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print("w = ", w, " Type of w = ", type(w), "\n\t", "x = ", x, " Type of x = ", type(x),"\n\t", "y = ", y, " Type of y = ", type(y), "\n\t", "z = ", z, " Type of z = ", type(z))

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print("x = ", x, " Type of x = ", type(x),"\n\t", "y = ", y, " Type of y = ", type(y), "\n\t", "z = ", z, " Type of z = ", type(z))
