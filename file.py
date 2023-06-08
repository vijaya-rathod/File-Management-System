import os
import shutil
import datetime

def create_file():
    #This code prompts the user to enter a file name and content. It then opens a new file with the specified name and writes the content to it. The file is automatically closed when the with block is exited.
    filename = input("Enter the file name: ")#defult txt
    filecontent = input("Enter the file content: ")

    with open(filename, 'w') as file:
        file.write(filecontent)
        
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