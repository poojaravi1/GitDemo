#readLines method stores the contents of the text file(everyline as one item in list) in list

file = open("test.txt")
for i in file.readlines():
    print(i)

