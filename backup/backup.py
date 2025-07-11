#!/usr/bin/env python3
"""
File Backup Script

Automates backing up files from one folder to another.
"""

import os
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    """
    Backup all files from source directory to destination directory.
    
    Args:
        source_dir (str): Path to source directory
        dest_dir (str): Path to destination directory
    """
    try:
        # Create destination directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)
        
        # Get list of files in source directory
        files = [f for f in os.listdir(source_dir) 
                if os.path.isfile(os.path.join(source_dir, f))]
        
        if not files:
            print(f"No files found in {source_dir}")
            return
        
        print(f"Starting backup of {len(files)} files from {source_dir} to {dest_dir}")
        
        # Copy each file
        for file in files:
            src_path = os.path.join(source_dir, file)
            dest_path = os.path.join(dest_dir, file)
            
            # Check if file already exists in destination
            if os.path.exists(dest_path):
                # Add timestamp to filename if file exists
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename, extension = os.path.splitext(file)
                dest_path = os.path.join(dest_dir, f"{filename}_{timestamp}{extension}")
            
            shutil.copy2(src_path, dest_path)
            print(f"Copied: {file}")
        
        print(f"Backup completed successfully. {len(files)} files copied.")
        
    except Exception as e:
        print(f"Error during backup: {str(e)}")

if __name__ == "__main__":
    # Configure your source and destination directories here
    SOURCE_DIRECTORY = "/path/to/source/folder"  # Update this path to your own
    DESTINATION_DIRECTORY = "/path/to/backup/folder"  # Update this path to your own
    
    # Validate paths
    if not os.path.isdir(SOURCE_DIRECTORY):
        print(f"Error: Source directory does not exist: {SOURCE_DIRECTORY}")
    else:
        backup_files(SOURCE_DIRECTORY, DESTINATION_DIRECTORY)