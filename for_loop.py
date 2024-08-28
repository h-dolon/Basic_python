# for items in ['dolon','sabah','jerin']:
#     print(items)
# for num in  range(5,10,2):
#     print(num) 

'''prices=[20,30,40]
total=0
for i in prices:
    total=total+i       
print(total)   ''' 

array1 = [1,3,5,7]
array2 = [2,4,6,8]
array3 = []
count = 0

# for dolon, sabah in enumerate(array1):
#     array3.append(array1[dolon])
#     array3.append(array2[dolon])

print("merged:", end="            ")
for i in range(4):
    print(array1[i], array2[i], end=' ')