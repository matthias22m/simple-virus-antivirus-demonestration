import hashlib
import os


def calculate_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buffer = file.read()
        hasher.update(buffer)
    return hasher.hexdigest()

# Path to the file to check
file_to_check = './dist/delete_files.exe'

# Calculate the hash of the file
file_hash = calculate_hash(file_to_check)

# Print the hash
print(f'The MD5 hash of {file_to_check} is: {file_hash}')