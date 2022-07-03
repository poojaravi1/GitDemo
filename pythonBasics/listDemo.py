values = [0, 1, "Pooja Ravi", 4.0, 'hi']

print(values[0])  #0
print(values[2])  #Pooja Ravi
print(values[4])  #hi
print(values[-1]) #hi
values.insert(3, 5)  #to inject new items in between/start/end of the list
print(values)
values.append("end")  #append value to the end of the list
print(values)

values[2] ="pooja"  #to update the existing list item with new item
print(values)

del values[0]
print(values)  #OP: [1, 'pooja', '5', 4.0, 'hi', 'end']