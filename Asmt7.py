#1.Concatenation and Slicing 
# Taking three string inputs
Str1 = input("Enter first string: ")
Str2 = input("Enter second string: ")
Str3 = input("Enter third string: ")

# Concatenating the first two strings
Concatenated_string = Str1 + Str2

# Slicing the concatenated string from index 2 to 8 (inclusive)
Sliced_string = Concatenated_string[2:9]

# Printing the concatenated and sliced strings
print('Concatenated String:', Concatenated_string)
print('Sliced String:', Sliced_string)

#2.Case Conversion
# Taking a string input
String = input('Enter a string: ')

# Converting to uppercase
Uppercase_str = String.upper()

# Converting to lowercase
Lowercase_str = String.lower()

# Swapping case of all characters
Swapped_case_str = String.swapcase()

# Checking if the string is in title case
Is_title_case = String.istitle()

# Printing the results
print('Uppercase:', Uppercase_str)
print('Lowercase:', Lowercase_str)
print('Swapped Case:', Swapped_case_str)
print('Is Title Case:', Is_title_case)


#3.String Search and Replace

# Taking a sentence input
Sentence = input('Enter a sentence: ')

# Searching for the word “Python”
Contains_python = 'Python' in Sentence

# Replacing “Python” with “Java”
Modified_sentence = Sentence.replace('Python', 'Java')

# Printing the results
print("Contains Python:", Contains_python)
print("“Modified Sentence:”", Modified_sentence)

#4 Count Specific Character 
# Taking a string input
String = input("Enter a string: ")

# Defining vowels
Vowels = 'AEIOUaeiou'

# Counting vowels, consonants, and spaces
Vowel_count = sum(1 for char in String if char in Vowels)
Consonant_count = sum(1 for char in String if char.isalpha() and char not in Vowels)
Space_count = String.count('')

# Printing the counts
print('Number of vowels:', Vowel_count)
print('Number of consonants:', Consonant_count)
print('Number of spaces:', Space_count)