import os #OS module in Python provides functions for interacting with the operating system

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)  #os.listdir function is used to list files in folder
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path) # , used to assign multiple values returned by a function to multiple variables in a single statement, error_message gets the value 'None' and files get files ki list as a value 
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()
