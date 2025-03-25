input_str=input("Enter a list of programs seperated by spaces:")
program_lst=input_str.split()
program_lst=[int(i) for i in program_lst]
print(program_lst)
print(type(program_lst))