def factorial(x):
    if x==1 or x==0:
        return 1
    else:
        #recursive call to a function
        return(x*factorial(x-1))
num=1
result=factorial(num)
print("the factorial of",num,"is",result)