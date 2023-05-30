# Ops 401 Challenge Day 31 
# Justin 'Sage'
# Utilized ChatGPT 
# Script prompts user to type in a file name to search for, prompts user for a directory in search in, searches each file in the directory by name, for each positive detection, prints the screen file name and location, and at the end prints to screen how many files were searches and how many hits were founds. 
import os

# Prompt the user to enter the file name to search for
file_name = input("Enter the file name to search for: ")

# Prompt the user to enter the directory to search in
directory = input("Enter the directory to search in: ")

# Initialize counters
total_files_searched = 0
hits_found = 0

# Search each file in the directory by name
for root, dirs, files in os.walk(directory):
    for file in files:
        if file == file_name:
            file_path = os.path.join(root, file)
            print("File found:", file_path)
            hits_found += 1
        total_files_searched += 1

# Print search results
print("Total files searched:", total_files_searched)
print("Hits found:", hits_found)
