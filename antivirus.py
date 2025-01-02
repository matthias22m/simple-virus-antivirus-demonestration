import hashlib
import os

virus_hashs = {'81043e8e3f0ddb1905485fab1131a1ca'} # Store the MD5 hash of every virus file we create
virus_files = []

def calculate_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buffer = file.read()
        hasher.update(buffer)
    return hasher.hexdigest()

directory_path = "."

for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_hash = calculate_hash(file_path)
        if file_hash in virus_hashs:
            virus_files.append(file_path)

if virus_files:
    print("The following files are infected with the virus:")
    for virus_file in virus_files:
        print(virus_file)
else:
    print("No virus found.")


permission = input("Enter Yes to delete the infected files: ")

if permission.lower() == "yes":
    for virus_file in virus_files:
        os.remove(virus_file)
        print(f"Deleted infected file: {virus_file}")
    print("All infected files have been deleted.")
input("Press Enter to exit...")