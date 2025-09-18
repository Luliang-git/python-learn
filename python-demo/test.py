# print("hello world")

# var1 = input("Enter something: ")
# var2 = input("Enter something else: ")
# print("You entered:", var1, "and", var2)

# varStr = "Beautiful is better than ugly Explicit is better than implicit Simple is better than complex."
# var3 = varStr.count("better")
# print("The word 'better' appears", var3, "times.")

# var4 = input("Enter a: ")
# var5 = input("Enter b else: ")
# print("a+b=", int(var4) + int(var5))


# print(123.0 == 123)
# print(123.0 > 123)
# print("ABC">123)


var6 = input("Enter a: ")
varOpt = input("Enter operator (+, -, *, /): ")
var7 = input("Enter b: ")
try:
    a = float(var6)
    b = float(var7)
    if varOpt == "+":
        print("a+b=", a + b)
    elif varOpt == "-":
        print("a-b=", a - b)
    elif varOpt == "*":
        print("a*b=", a * b)
    elif varOpt == "/":
        if b != 0:
            print("a/b=", a / b)
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operator")
except ValueError:
    print("Invalid input: please enter numbers.")