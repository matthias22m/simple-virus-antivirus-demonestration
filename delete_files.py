import os

def delete_all_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print(f"Deleted file: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    delete_all_files_in_directory(current_directory)