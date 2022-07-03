it = 4

while (it > 0):
    it = it - 1
    print(it)
print("***************************8")
num = 5
while (num > 1):
    if num == 2:
        break
    else:
        num = num -1
        print(num)

print("************SKIPPING A SPECIFIC NUMBER***************8")

num = 10
while (num > 1):
    if num == 3:
        num = num -1
        continue
    num = num -1
    print(num)
