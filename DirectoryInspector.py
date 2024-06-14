import os

def list_directory_contents(path):
    files = []
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                files.append(entry.name)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Contents of the directory:")
        for file in files:
            print(file)

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    list_directory_contents(directory_path)
