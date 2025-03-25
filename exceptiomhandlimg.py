#Built in exception
#Zero Division error
#Value error
#key error
#file Not Found
#Timeout error
#Type zero
#Index out range

#try-catch-exception
#Hadnling multiple exception
#Raising Exception raise ValueError("Age must be 18 or above")
#custom Exception/user-defined exception
#use log file
try:
    lst=[1,2]
    var=lst[2]
    print(var)
except Exception as e:
    print(e)
    with open("D:/textfiles/log_563",'w') as log:
        log.write(f"{e}")
finally:
    print('I am In Exception block')

#Handling Multiple Exceptionss
#Advantages
#Prevents application crashes
#Improves the user exprience
#Simplifies,security
#easily debug it