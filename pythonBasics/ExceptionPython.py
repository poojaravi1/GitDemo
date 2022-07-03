
ItemsInCart = 0

if ItemsInCart != 2:
    #raise Exception("Must add exactly 2 items in cart")
    pass

#assert (ItemsInCart == 2)

try:
    with open("log.txt", 'r') as reader:
        reader.readline()

#except:
    #print("No file present. customized message")


except Exception as e:
    print(e)



