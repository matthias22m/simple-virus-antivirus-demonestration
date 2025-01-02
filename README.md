# Virus and Antivirus Demonstration

## Requirements

1. Python 3.x
2. PyInstaller

## Setup

1. Clone the repository or download the files to your local machine.
2. Ensure you have Python 3.x installed on your system.
3. Install PyInstaller if you haven't already:
   ```bash
   pip install pyinstaller
   ```

## Files

- `delete_files.py`: Script to delete all files in the current directory.
- `antivirus.py`: Script to detect and delete files with specific virus hashes.
- `chech_virus_hash.py`: Script to calculate the MD5 hash of a file.
- `create_exe_instructions.txt`: Instructions to create executable files from the Python scripts.

## Steps to Demonstrate

### 1. Create Executable for `delete_files.py`

1. Navigate to the directory containing your Python script:
   ```bash
   cd /C:/Users/hhhhhp/Desktop/Viruss
   ```

2. Run PyInstaller to generate the executable:
   ```bash
   pyinstaller --onefile delete_files.py
   ```

3. After the process completes, you will find the executable file in the `dist` directory.

### 2. Calculate the Hash of the Executable

1. Run the `chech_virus_hash.py` script to calculate the MD5 hash of the `delete_files.exe` file:
   ```bash
   python chech_virus_hash.py
   ```

2. Note the MD5 hash printed by the script.

### 3. Update `antivirus.py` with the Virus Hash

1. Add the MD5 hash of the `delete_files.exe` file to the `virus_hashs` set in `antivirus.py`:
   ```python
   virus_hashs = {'<your_calculated_hash>'}
   ```

### 4. Run the Antivirus Script

1. Run the `antivirus.py` script to scan the directory for the virus:
   ```bash
   python antivirus.py
   ```

2. If the script detects the virus, it will list the infected files and prompt you for permission to delete them.

3. Enter `Yes` to delete the infected files.

### Conclusion

This demonstration shows how to create a virus file, calculate its hash, and use an antivirus script to detect and delete the virus. Ensure you follow the steps carefully to understand the process.
