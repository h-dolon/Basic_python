user_defined_range=int(input('Enter a namber:'))
def summation(num):
    sum=0
    for i in range(num+1):
        sum=sum+i
        i+=1
    return sum
sum=summation(user_defined_range)
print(sum)        