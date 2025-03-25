# 1.Variables in python doesn't need explicit declaration.So python is dynamically typed language.
# x=10//x is integer
# x=”Hello”//x is string
# 2.Web development, Machine learning,GUI, Data science are the areas Python widely used
# 3.Reference Cycle: Python uses a reference count mechanism to track the number of
# references to an object
# Example:
# a=[]
# b=[a]
# a.append(b)#Reference cycle a->b->a
# del a,b #garbage collector handles the cycle
# 4.gc.collect: python includes garbage collector to reclaim or unused memory
# It removes the object that are no longer reachable such as objects reference cycle
# Import gc
# gc.collect # triggered garbage collector
# 5.Python automatic because simplifies repetitive tasks with minimal code