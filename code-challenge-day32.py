import os
import hashlib
import time

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
            
            # Generate the file's MD5 hash
            with open(file_path, 'rb') as f:
                md5_hash = hashlib.md5(f.read()).hexdigest()
            
            # Get file size
            file_size = os.path.getsize(file_path)
            
            # Get current timestamp
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            
            # Print file information
            print("Timestamp:", timestamp)
            print("File Name:", file)
            print("File Size:", file_size, "bytes")
            print("File Path:", file_path)
            print("MD5 Hash:", md5_hash)
            print()
            
            hits_found += 1
        total_files_searched += 1

# Print search results
print("Total files searched:", total_files_searched)
print("Hits found:", hits_found)
