import os
dir_path = "C:\\Users\\YourUsername\\Documents\\MyNewDirectory"

try:
    os.mkdir(dir_path)
    print(f"Directory created: {dir_path}")
except FileExistsError:
    print(f"Directory already exists: {dir_path}")
except OSError as e:
    print(f"Error creating directory: {e}")