# FILE-INTEGRITY-CHECKER

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**:  Shravani Jamdade

**INTERN ID**: CT08JMK

**DOMAIN**: Cyber Security & Ethical Hacking

**BATCH DURATION**:January 5th, 2025 to February 5th, 2025

**MENTOR NAME**: NEELA SANTOSH

#CODE 
import hashlib
import os
import time

# Function to calculate the hash value of a file
def calculate_hash(file_path, hash_algo='sha256'):
    hash_obj = hashlib.new(hash_algo)
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):  # Reading in chunks
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# Function to check the integrity of files in a directory
def check_file_integrity(directory_path, hash_algo='sha256'):
    file_hashes = {}
    
    # Iterate through the files in the given directory
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            # Skip directories, only process files
            if os.path.isfile(file_path):
                file_hashes[file_path] = calculate_hash(file_path, hash_algo)
    
    return file_hashes

# Function to compare current and saved hashes
def compare_hashes(old_hashes, new_hashes):
    changes_detected = False
    
    # Check for any changes or missing files
    for file_path, hash_value in new_hashes.items():
        if file_path not in old_hashes:
            print(f"New file detected: {file_path}")
            changes_detected = True
        elif old_hashes[file_path] != hash_value:
            print(f"File modified: {file_path}")
            changes_detected = True

    # Check for deleted files
    for file_path in old_hashes:
        if file_path not in new_hashes:
            print(f"File deleted: {file_path}")
            changes_detected = True
    
    return changes_detected

# Main function to monitor changes in files
def monitor_directory(directory_path, hash_algo='sha256', check_interval=10):
    print(f"Monitoring directory: {directory_path}")
    old_hashes = check_file_integrity(directory_path, hash_algo)
    
    while True:
        time.sleep(check_interval)  # Wait for the specified interval before checking again
        print(f"\nChecking for changes...")
        
        new_hashes = check_file_integrity(directory_path, hash_algo)
        if compare_hashes(old_hashes, new_hashes):
            print("Changes detected!")
        else:
            print("No changes detected.")
        
        old_hashes = new_hashes  # Update the old hash values to the new ones for the next comparison

# Example usage: Monitor a directory for file changes
if __name__ == "__main__":
    directory_to_monitor = "./test_directory"  # Replace with the directory you want to monitor
    monitor_directory(directory_to_monitor)
#OUTPUT
Monitoring directory: ./test_directory

Checking for changes...
No changes detected.

Checking for changes...
File modified: ./test_directory/example.txt

Checking for changes...
No changes detected.

















