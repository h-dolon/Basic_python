# numbers=[2,3,4,3,2,6,2]
# for i in numbers:
#     count_number=numbers.count(i)
#     if count_number>1:
#         numbers.remove(i)
#     i+=1
# print(numbers)   


numbers=[2,3,4,3,2,6,2]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)        