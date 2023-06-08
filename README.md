

# File-Management-System

## Table of Contents

- Importing the libraries
- File creation
- Directory creation
- File search
- File deletion
- File editing
- File information
- File movement
## import the libraries
``` shell
import os
import shutil
import datetime
```
os: This library provides a way of interacting with the operating system. We can use it to perform various operations like create, rename or delete files and directories, get information about a file, list the contents of a directory, etc.

shutil: This library provides high-level operations on files and collections of files. We can use it to copy, move, rename, or delete files and directories.

datetime: This library provides classes for working with dates and times. We can use it to get the current date and time, format dates and times, perform arithmetic on dates and times, etc.

## File creation
### Users can create new files and provide them with a name and content.
``` shell
def create_file():
    #This code prompts the user to enter a file name and content. It then opens a new file with the specified name and writes the content to it. The file is automatically closed when the with block is exited.
    filename = input("Enter the file name: ")#defult txt
    filecontent = input("Enter the file content: ")

    with open(filename, 'w') as file:
        file.write(filecontent)
 ```
The time complexity of this function is O(1) because it has a constant number of operations, regardless of the size of the input. The function takes input from the user and writes it to a file using the 'open()' and 'write()' functions.

## Directory creation
### Users can create new directories and organize files within them.
``` shell
def create_directory():
    #This code creates a new directory with given name if it doesn't already exist, and then moves all files ending in ".txt" into that directory. We can modify the code to move files based on different criteria.
    # Create a new directory
    new_dir = input("Enter the directory name:")
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        print("Directory", new_dir, "created.")
    else:
        print("Directory", new_dir, "already exists.")
    # Move files into the new directory
    file_list = os.listdir()
    for file in file_list:
        if os.path.isfile(file):
            if file.endswith(".txt"):
                shutil.move(file, new_dir)
                print(file, "moved to", new_dir)
 ```
 The time complexity of this function is O(n), where n is the number of files in the current directory. The function first creates a new directory and obtains a list of all files in the current directory using 'os.listdir()'. This operation takes O(n) time, where n is the number of files in the directory. Then, the function iterates over each file in the directory and checks if it is a file and ends with ".txt". Finally, for each file that meets the criteria, the function moves it to the new directory using 'shutil.move()'.The overall time complexity of the function is O(n)
 
 
 ## Search files
 ### Users can search for files by name or content and retrieve a list of matching files.
 ``` shell
 def search_file():
    search_term = 'india'
    search_directory = r'C:\Users\ADMIN\Desktop\collage'
    matching_files = []
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            if search_term in file:
                matching_files.append(os.path.join(root, file))
            else:
                with open(os.path.join(root, file), 'r') as f:
                    file_contents = f.read()
                    if search_term in file_contents:
                        matching_files.append(os.path.join(root, file))
    for k in matching_files:
        print(k)        
 ```
 The time complexity of this function is O(n* m), where n is the number of files and directories in the search_directory and m is the size of the largest file in the directory. The function first initializes an empty list called 'matching_files'. Then, the function uses 'os.walk()' to traverse the directory tree rooted at 'search_directory'. This operation takes O(n) time, where n is the number of files and directories in the tree. For each file in the directory tree, the function checks if the search term is in the filename. If the search term is in the filename, the function appends the file path to the 'matching_files' list. If the search term is not in the filename, the function reads the file and checks if the search term is in the file contents. This operation takes O(m) time, where m is the size of the file. If the search term is in the file contents, the function appends the file path to the 'matching_files' list. Finally, the function prints all the file paths in the 'matching_files' list, which takes O(n) time, where n is the number of matching files. Therefore, the overall time complexity of the function is O(n* m).
 
 
 ## File deletion
 ### Users can delete existing files and directories. Deleting a directory should also remove all the files and subdirectories within it.
 ``` shell
 def delete_file_or_directory():
    # Function to delete a .txt file or a directory
    a=int(input("Enter 1.delete using file name 2.Delete using path"))
    if(a==1):
        filename = input("Enter the name of the file to delete: ")
        try:
            os.remove(filename)
            print(f"{filename} has been deleted successfully!")
        except FileNotFoundError:
            print(f"{filename} does not exist in the current directory.")
        except Exception as ex:
            print(f"An error occurred: {ex}")
    else:
        path=input("Enter the file path:")
        try:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
            print(f"Successfully deleted {path}")
        except OSError as e:
            print(f"Error occurred while deleting {path}: {e.strerror}")
 ```
 The time complexity of this function is O(1) for the first part of the function, where the user inputs whether to delete using file name or path. This operation takes a constant amount of time, regardless of the input. If the user chooses to delete using file name, the time complexity of deleting the file is O(1), as the `os.remove()` function takes a constant amount of time to delete a file. If the user chooses to delete using file path, the time complexity of deleting the file or directory depends on whether it is a file or directory. If it is a file, the time complexity is also O(1), as the `os.remove()` function is used to delete the file. However, if it is a directory, the `shutil.rmtree()` function is used to delete the directory and all its contents, which takes O(n) time, where n is the number of files and directories within the directory being deleted. Therefore, the overall time complexity of this function can range from O(1) to O(n), depending on the user input and whether a directory needs to be deleted.
 
 
 ## File editing
 ### Users can edit the content of existing files.
 ``` shell
 def edit_file(): 
    # Open the file in write mode
    name=input("Enter existing file name on this directory:")
    content=input("Enter new content:")
    with open(name, 'w') as f:
        # Write the new content to the file
        f.write(content)

    # Open the file in read mode
    with open(name, 'r') as f:
        # Print the file contents
        print(f.read())
 ```
 The time complexity of this function is O(n), where n is the length of the new content being written to the file. The function first takes input from the user for the file name and new content, which takes a constant amount of time. Next, the function opens the file in write mode using `open()` and writes the new content to the file using `write()`. Writing to a file takes O(n) time, where n is the length of the new content being written. The function then opens the same file in read mode and prints its contents using `read()`. Reading from a file takes O(m) time, where m is the length of the file contents. Therefore, the overall time complexity of the function is O(n + m), but since n is generally smaller than m, we can approximate the time complexity as O(m).
 

 ## File information
 ### Users can view information about files, including their name, size, creation date, and last modification date.
 ``` shell
 def get_file_info():
    # Enter the path to the directory you want to view
    directory_path = input("Enter the path:")
    # Loop through each file in the directory
    for filename in os.listdir(directory_path):
        # Get the full path of the file
        filepath = os.path.join(directory_path, filename)

        # Get file size in bytes
        filesize = os.path.getsize(filepath)

        # Get file creation time and format it
        created = os.path.getctime(filepath)
        created_formatted = datetime.datetime.fromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S')

        # Get file last modification time and format it
        modified = os.path.getmtime(filepath)
        modified_formatted = datetime.datetime.fromtimestamp(modified).strftime('%Y-%m-%d %H:%M:%S')

        # Print the file information
        print("File name: {}".format(filename))
        print("File size: {} bytes".format(filesize))
        print("Created: {}".format(created_formatted))
        print("Last modified: {}".format(modified_formatted))
 ```
 The time complexity of this code is O(n), where n is the number of files in the directory. The loop iterates through each file in the directory, and for each file, it calls the `os.path.getsize()`, `os.path.getctime()`, and `os.path.getmtime()` functions, which are all O(1) operations. Therefore, the overall time complexity of the code is O(n)
 

 ## File movement
 ### Users can move files between directories.
 ``` shell
 def move_file():
    source_dir = input("Enter path to source directory:")
    dest_dir = input("Enter path to destination directory:")

    # Set the file extension to search for
    file_ext = input("Enter the extention of file Ex:'.txt' to search:")

    # Get a list of all files in the source directory
    files = os.listdir(source_dir)
    try:
        # Loop through each file and move it to the destination directory if it has the right file extension
        for file in files:
            if file.endswith(file_ext):
                src_path = os.path.join(source_dir, file)
                dest_path = os.path.join(dest_dir, file)
                shutil.move(src_path, dest_path)
        print("successfully moved !")
    except:
        print("Error occured")
 ```
 The time complexity of this code is O(n), where n is the number of files in the source directory. The loop iterates through each file in the directory, and for each file, it checks if it has the right file extension, which is an O(1) operation. If the file has the right extension, it calls the `shutil.move()` function, which is also an O(1) operation. Therefore, the overall time complexity of the code is O(n).
 

 
 ## Calling the functions
 ``` shell
 while(True):
    n=input("Choose 1.create file 2.create directory 3.search file 4.Delete file or directory 5.Edit file 6. File info 7.Move file 8.Exit")
    if(n=='1'):
        create_file()
    elif(n=='2'):
        create_directory()
    elif(n=='3'):
        search_file()
    elif(n=='4'):
        delete_file_or_directory()
    elif(n=='5'):
        edit_file()
    elif(n=='6'):
        get_file_info()
    elif(n=='7'):
        move_file()
    elif(n=='8'):
        break
    else:
        print("Enter valid input")
 ```
 This is the program for file manageent system
