#Create and Write to a file:
# Create and write to myfile.txt
with open('myfile.txt', 'w') as file:
    file.write('Hello, this is a file handling assignment.\n')
    file.write('Python makes it easy to work with files.\n')


#2.Read and display files content:
# Read and display the content of myfile.txt
with open('myfile.txt', 'r') as file:
    Content = file.read()
    print(Content)

#3.Append data to an existing file

# Append data to myfile.txt
with open('myfile.txt', 'a') as file:
    file.write('This is an appended line.\n')

# Read and display the updated content
with open('myfile.txt', 'r') as file:
    Updated_content = file.read()
    print(Updated_content)

#4.Count the number of words  in a file
# Count the number of words in myfile.txt
with open('myfile.txt', 'r') as file:
    Text = file.read()
    Word_count = len(Text.split())
    print('Total word count:', Word_count)



# Copy content from myfile.txt to copy.txt
with open('myfile.txt', 'r') as source_file:
    Content = source_file.read()

with open('copy.txt', 'w') as target_file:
    target_file.write(Content)

# Verify the copied content
with open('copy.txt', 'r') as copied_file:
    Copied_content = copied_file.read()
    print('Copied file content:\n', Copied_content)