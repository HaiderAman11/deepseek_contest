import os

def deep_seek_search(folder_path, keyword):
    """
    Searches through all files in a folder for a specific keyword and counts occurrences.
    """
    matches = {}

    # Loop through all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"Reading file: {file_path}")  # Debugging: Show which file is being read
            
            try:
                # Open and read the file
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    # Count how many times the keyword appears
                    count = content.lower().count(keyword.lower())
                    if count > 0:
                        matches[file_path] = count
            except:
                # Skip files that can't be read (e.g., binary files)
                print(f"Skipping file (cannot read): {file_path}")  # Debugging: Show skipped files
                pass

    return matches

# Input: Folder path and keyword to search
folder_path = input("Enter the folder path to search: ")
keyword = input("Enter the keyword to search for: ")

# Perform the search
results = deep_seek_search(folder_path, keyword)

# Display the results
if results:
    print(f"Found '{keyword}' in the following files:")
    for file_path, count in results.items():
        print(f"- {file_path}: {count} times")
else:
    print(f"No files found containing '{keyword}'.")