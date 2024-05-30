# Dictionary is ordered collection for python version 3.7 onwards

dict = {'Name': 'Pooja', 'Age': 25, 'Surname':'Jagtap'}
print(dict.keys())
print(dict.values())
print(dict.items())

for key in dict.keys():
    print(f'The value corresponding to the key {key} is {dict[key]}')

print("************************************************************************")
#
# for key,value in dict.items():
#     print(f'The value corresponding to the key {key} is {value}')

dict1= {101: 65,102: 69, 103: 89}
dict2= {104: 87, 105: 90}
dict1.update(dict2)
print(dict1)
