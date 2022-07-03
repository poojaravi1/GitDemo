names = ['abc', 'def', 'try.uio', 'dschjb']
for i in names:
    print(i)
print('#' * 40)

nums = [1, 4, 7, 9, 8]
for k in nums:
    print(k)

print('#' * 40)

#print summation of first 5 natural numbers
summation = 0
for m in range(1, 6):
    summation = summation + m
print(summation)

print("***************SKIPPING WITH SPECIFIC ITERATION COUNT****************")

for n in range(1,10,2):
    print(n)

print("***************SKIPPING FIRST INDEX****************")
for l in range(10):
    print(l)