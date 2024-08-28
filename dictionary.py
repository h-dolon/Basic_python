# cutomer={
#     'name':'HOssna ara',
#     'age': 25,
#     'home town':'Dinajpur',
#     'is_varified': True 

# }
# print(cutomer.get('is_varified'))

phone=input('phone')
digits={
    '1':'one',
    '2':'two',
    '3':'three'
}
output=''
for ch in phone:
    output=output+digits.get(ch)+' '
print(output)    