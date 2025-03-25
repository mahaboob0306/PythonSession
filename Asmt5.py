#Tuple Manipulation:
# Create a tuple of your favorite movies
movies = ("Inception", "Interstellar", "The Dark Knight", "Avengers", "Titanic")
# Print the length of the tuple
print("Length of the tuple:", len(movies))
# Access and print the second movie in the tuple
print("Second movie:", movies[1])
# Create a new tuple containing the first three movies from the original tuple
new_tuple = movies[:3]
print("First three movies:", new_tuple)
#Set Operations:
# Create two sets of integers
set1 = {1, 2, 3, 4, 5}
set2 = {3,4, 5, 6, 7}

# Find and print the intersection of set1 and set2
intersection = set1 & set2
print("Intersection:", intersection)
#Remove Duplicate elements from the from two sets
duplicateremove =set1.difference_update(intersection)
print("duplicateremove:", duplicateremove)
{3,4,5}
# Find and print the elements that are in set1 but not in set2
difference = set1 - set2
print("Elements in set1 but not in set2:", difference)
{1,2,3,6,7}
# Add the number 8 to set1
set1.add(8)
print("Updated set1:", set1)
{1,2,3,4,5,8}
#Tuple and set conversation
# Create a list of fruits
fruits = ["apple", "banana", "cherry", "apple", "orange", "banana"]
# Convert the list into a tuple
fruits_tuple = tuple(fruits)
print("Tuple:", fruits_tuple)
# Convert the tuple into a set
fruits_set = set(fruits_tuple)
{"apple","banana","cherry", "orange"}
# Print the resulting set (duplicates removed)
print("Set:", fruits_set)
{"banana","apple"}

