#FileHandling: Divide Zero error write a file and read a file
#where file handling is used are below points
#1.Log Files:Record activites in a system log
#2.Data Processing:
#3.FileBackups


# Modes in which is file is opened 

# r:read a file
# w:write a file
# a:append a file
# b:binary mode




#open the file and read the file

# f = open("D:/textfiles/Sample_170325.txt",'r')
# # get_text=f.read()
# # get_text=f.readline()
# get_text=f.readlines()
# f.close()
# # for line in get_text:
# #     print(line.strip())
# print(get_text)
# # for x in get_text:
# #     print(x)

#to write the file
# f=open("D:/textfiles/Sample_170325.txt",'w')
# f=open("D:/textfiles/Sample_170325.txt",'a')
# get_text=f.write("This is python Training Session")
# f.close()


#if we want to write in multiple lines than
# f=open("D:/textfiles/Sample_170325.txt",'w')
# lines=["Line 1\n","Line 2\n","Line 3\n"]
# get_text=f.writelines(lines)
# f.close()


#Explicitly file will closed we no need to write implicitly
# with open("D:/textfiles/Sample_170325.txt",'w') as file:
#     lines=["Line 1\n","Line 2\n","Line 3\n","Line 4\n","Line 5\n"]
#     file.writelines(lines)

#if want to read & copy the file from the above file and write to another file

#copy one file to another file 
# with open("D:/textfiles/Sample_170325.txt",'r') as source ,open("D:/textfiles/Sample2_170325.txt",'w') as dest:
#     for line in source:
#         dest.write(line)

#To count the number of words
# with open("D:/textfiles/Sample2_170325.txt",'r') as file:
#     content = file.read()
#     words   =content.split()
#     print(f"Numbers of words count {len(words)} in file")

#Reading a Binary file rb is used for  non text file
# with open('D:/textfiles/download.jpg',"rb") as file:
#     data =file.read()
#     print(f"Read the Binary {len(data)} bytes")

#writing in log files when exception gets

x=int(input("Enter the first number :"))
y=int(input("Enter the second number:"))
try:
    result=x/y
except ZeroDivisionError as e:
    print(e)
    with open('D:/textfiles/log_170329.txt','w') as log:
        log.write("This is Division by Zero error")

