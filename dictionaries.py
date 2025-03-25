dic={'name':'noor','age':24,'city':'Hyderabad','address':'kukatpally'}
print(dic['name'])
#get values using get
print(dic.get('city'))
print(dic.get('pincode','Not Found'))
dic['pincode']="78665"
print(dic)
dic['age']=98
print(dic)
dic.pop('address')
print(dic)
del dic['age']
print(dic)
dic.clear()
print(dic)
#for loop for key and values
# dic={'name':'noor','age':'24','city':'Hyderabad','address':'kukatpally'}
# for key in dic.keys():
#     print(key)
# for value in dic.values():
#     print(value)
# for key,value in dic.items():
#     print(f"{key}:{value}")


# country=['India','Pakista','Australia']
# print(country[0])
# country={'IND':'India','PAK':'Pakistan','AUS':'Australia'}
# print(country['IND'])

#capital of country
country={'India':'India','Pakistan':'Islamabad','AUS':'Cidney'}
for key in country.keys():
    print(key)
for value in country.values():
    print(value) 
for key,value in country.items():
    print(f"{key}:{value}")