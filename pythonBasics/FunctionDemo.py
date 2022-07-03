
def GreetMe(name):
    print("Happy Morning " + name)
    #function call

GreetMe("Pooja Ravi")

# Add 2 numbers

def AddTwoNumbers(a, b):
    print(a + b)
try:
    a = int(input("Enter first number to add "))
    b = int(input("Enter second number to add "))
    AddTwoNumbers(a, b)

except:
    print("Only integers allowed")