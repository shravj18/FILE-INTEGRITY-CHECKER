#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import os
import json

HASH_ALGORITHM = "sha256"  # Change to 'md5', 'sha1', etc., if needed
HASH_FILE = "file_hashes.json"

def calculate_hash(file_path, algorithm=HASH_ALGORITHM):
    """Calculate hash of a file using the specified algorithm."""
    hasher = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def save_hashes(directory):
    """Generate and save hashes of all files in a directory."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_hash(file_path)
    
    with open(HASH_FILE, "w") as f:
        json.dump(file_hashes, f, indent=4)
    print("Hashes saved successfully.")

def verify_integrity():
    """Verify file integrity by comparing current hashes with saved ones."""
    if not os.path.exists(HASH_FILE):
        print("No hash file found. Please generate hashes first.")
        return
    
    with open(HASH_FILE, "r") as f:
        saved_hashes = json.load(f)
    
    for file_path, saved_hash in saved_hashes.items():
        if not os.path.exists(file_path):
            print(f"MISSING: {file_path}")
            continue
        current_hash = calculate_hash(file_path)
        if current_hash != saved_hash:
            print(f"MODIFIED: {file_path}")
        else:
            print(f"UNCHANGED: {file_path}")

def main():
    print("File Integrity Checker")
    print("1. Save hashes")
    print("2. Verify integrity")
    choice = input("Enter choice: ")
    
    if choice == "1":
        directory = input("Enter directory to monitor: ")
        save_hashes(directory)
    elif choice == "2":
        verify_integrity()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()


# In[ ]:




