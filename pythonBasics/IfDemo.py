#we input a number check if the number is positive or negative or zero and display an appropriate message

try:
    number1 = int(input("Enter a number : "))

    if number1 >= 0:
        if number1 == 0:
            print("Zero")
        else:
            print("Entered number", number1, "is positive")


    else:
        print("Entered number", number1, "is negative")

except:
    print("Enter only Integers. No other data types are allowed")