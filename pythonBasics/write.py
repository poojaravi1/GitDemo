#read the file and store all the lines in list
#reverse the list
#write the list back to the file

with open("test.txt", "r") as reader : #reader is our object here #is used so that this one step will take care of opening and closing the file (here text file)
    content = reader.readlines()
    reversed(content) #reverses content in file
    with open("test.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)
