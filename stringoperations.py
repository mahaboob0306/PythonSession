firstname='NoorShaba'
LastName='Mahaboob'
fullname=firstname+""+LastName
print(fullname)

greatings="Hello!"
repeat_greating=greatings * 3
print(repeat_greating)

#indexing
text="python"
print(text[0])
print(text[-1])

#slicing
text="Python training Program"
print(text[0:6])
print(text[7:])
print(text[-7:])
#reverse of a string 
print(text[::-1])

#Built in methods

text="python full stack programing"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

text='123abc'
print(text.isalpha())
print(text.isdigit())
print('123'.isalpha())

text='Python is a versatile programing language'
print(text.replace('programing','scripting'))
print(text.split())
split_words=text.split()
for items in split_words:
    print(items)

print('-'.join(text))

#String Formating
name='NoorShabaMahaba'
age=32
print(f"My name is {name} and i am {age} Young")
print("My name is {} and i am {} Young".format(name,age))

#position and arguments
print("My name is {name} and i am {age} Young".format(age=age,name=name))

#%percentage formate
name="NoorShab"
score=98
print('Hello %s,you score %d'%(name,score))

