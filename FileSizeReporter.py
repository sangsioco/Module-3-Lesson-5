import os
from collections import defaultdict

def count_file_extensions(directory):
    extension_counts = defaultdict(int)
    
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    _, extension = os.path.splitext(entry.name)
                    if extension:
                        extension = extension.lower()
                        extension_counts[extension] += 1

        print("File extension counts:")
        for ext, count in extension_counts.items():
            print(f"{ext.upper()}: {count}")
    
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{directory}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    count_file_extensions(directory_path)
