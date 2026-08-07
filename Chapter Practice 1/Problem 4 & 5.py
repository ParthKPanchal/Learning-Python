import os

# Select the directory whose content you want to list
directory_path='/php'

# Use the os module to list the directory content
contents=os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)