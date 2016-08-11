print "Welcome to my calculator, it can only perform basic math such as +, -, *, /,, enjoy :)"
print "Please puch in the numbers you want to calculate-->>"
while True:

    x = raw_input("Please punch in the first number!")
    y = raw_input("Please punch in the second number!")
    operator = raw_input("Please punch in youre operator!")
    x = float(x)
    y = float(y)

    if operator == "+":
        print x + y
    elif operator == "-":
        print x - y
    elif operator == "*":
        print x * y
    elif operator == "/":
        print x / y
