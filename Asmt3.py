#1.List Operations:
Num=[1,5,7,9]
Num.append(8)
Num.remove(9)
Num.sort()
print(Num)

#2.Dictionary Manipulation
Student={"name":'Noor',"age":23,"grade":'A+'}
Student['name']='Annu'#add a new student
Student['grade']='A1'#update grade
print(Student)
#3.Conditional-Statements(if-else)
Num1=int(input('Enter a number'))
if(Num1%2==0):
     print("given number is even number")
else:
     print("given number odd number")
#.basic for loop to print 1 to 5 number
for i in range(1,6):
  print("i values:::",i)