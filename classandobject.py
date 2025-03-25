name="shaba"
age=25
salary=55000
def employe_details(name,age,salary):
    print(f"Name:{name},Age:{age},salary:{salary}")

employe_details(name,age,salary)

#Above code procedural oritented language

class employee:
    def __init__(self,name,age,salary):
        #current instance of object to which memory this belongs
        self.name=name,#instance variable
        self.age=age,
        self.salary=salary#constructor method
        print("I am in constructor")
    # def employee_details(self):
    #     print(f"Name:{name},Age:{age},Salary:{salary}")#Instance Method 
    def __str__(self):
       return(f"Name:{name}") #  def __str__() what should be defined and returned when class and object 
obj=employee('Ram',23,60000)#Object creation
#obj.employee_details()#calling method from object
        
#Modifying object
obj.age=87

 #https://training.mind2i.com/batch-recordings/pfsp-eng_2025-01-20_08:00%20PM

