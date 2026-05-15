 import os
import shutil
import hashlib
from datetime import datetime

# =============================
# ADVANCED FILE ORGANIZER PRO
# =============================

# File Categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Python Files": [".py"],
    "Web Files": [".html", ".css", ".js"],
}

# =============================
# GET FILE HASH
# =============================

def get_file_hash(filepath):
    hasher = hashlib.md5()

    try:
        with open(filepath, 'rb') as file:
            
        # Advanced File Organizer Pro — Full Professional Python Project

## File Name

```bash
advanced_file_organizer_pro.py
```

---

# Full Python Code

```python
import os
import shutil
import hashlib
from datetime import datetime

# =============================
# ADVANCED FILE ORGANIZER PRO
# =============================

# File Categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Python Files": [".py"],
    "Web Files": [".html", ".css", ".js"],
}

# =============================
# GET FILE HASH
# =============================

def get_file_hash(filepath):
    hasher = hashlib.md5()

    try:
        with open(filepath, 'rb') as file:
            buffer = file.read()
            hasher.update(buffer)
        return hasher.hexdigest()

    except Exception:
        return None

# =============================
# CREATE LOG FILE
# =============================

def write_log(message, log_path="organizer_log.txt"):
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] {message}\n")

# =============================
# CREATE FOLDERS
# =============================

def create_folders(base_path):
    for folder in FILE_CATEGORIES.keys():
        folder_path = os.path.join(base_path, folder)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            write_log(f"Created folder: {folder}")

    others_path = os.path.join(base_path, "Others")

    if not os.path.exists(others_path):
        os.makedirs(others_path)
        write_log("Created folder: Others")

    duplicate_path = os.path.join(base_path, "Duplicates")

    if not os.path.exists(duplicate_path):
        os.makedirs(duplicate_path)
        write_log("Created folder: Duplicates")

# =============================
# ORGANIZE FILES
# =============================

def organize_files(base_path):

    moved_count = 0
    duplicate_count = 0
    skipped_count = 0

    file_hashes = {}

    print("\n====================================")
    print(" ADVANCED FILE ORGANIZER PRO")
    print("====================================\n")

    create_folders(base_path)

    for filename in os.listdir(base_path):

        file_path = os.path.join(base_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Skip this script
        if filename == os.path.basename(__file__):
            continue

        extension = os.path.splitext(filename)[1].lower()

        moved = False

        # =============================
        # CHECK DUPLICATES
        # =============================

        file_hash = get_file_hash(file_path)

        if file_hash:
            if file_hash in file_hashes:

                duplicate_folder = os.path.join(base_path, "Duplicates")
                destination = os.path.join(duplicate_folder, filename)

                shutil.move(file_path, destination)

                duplicate_count += 1

                write_log(f"Duplicate moved: {filename}")

                print(f"[DUPLICATE] {filename} moved to Duplicates")

                continue

            else:
                file_hashes[file_hash] = filename

        # =============================
        # ORGANIZE BY CATEGORY
        # =============================

        for folder, extensions in FILE_CATEGORIES.items():

            if extension in extensions:

                destination_folder = os.path.join(base_path, folder)
                destination = os.path.join(destination_folder, filename)

                shutil.move(file_path, destination)

                moved = True
                moved_count += 1

                write_log(f"Moved {filename} to {folder}")

                print(f"[MOVED] {filename} → {folder}")

                break

        # =============================
        # UNKNOWN FILE TYPES
        # =============================

        if not moved:

            others_folder = os.path.join(base_path, "Others")
            destination = os.path.join(others_folder, filename)

            try:
                shutil.move(file_path, destination)

                moved_count += 1

                write_log(f"Moved unknown file {filename} to Others")

                print(f"[OTHERS] {filename} → Others")

            except Exception as error:

                skipped_count += 1

                write_log(f"Skipped {filename}: {error}")

                print(f"[ERROR] Could not move {filename}")

    # =============================
    # FINAL SUMMARY
    # =============================

    print("\n====================================")
    print(" ORGANIZATION COMPLETED")
    print("====================================")

    print(f"Files Organized : {moved_count}")
    print(f"Duplicates Found: {duplicate_count}")
    print(f"Skipped Files   : {skipped_count}")

    write_log("Organization completed successfully")

# =============================
# MAIN PROGRAM
# =============================

def main():

    print("\n===== FILE ORGANIZER AUTOMATION TOOL =====\n")

    folder_path = input("Enter folder path to organize: ").strip()

    if not os.path.exists(folder_path):
        print("\n[ERROR] Invalid folder path!")
        return

    organize_files(folder_path)

    print("\nThank you for using Advanced File Organizer Pro!")

# =============================
# RUN PROGRAM
# =============================

if __name__ == "__main__":
    main()
```

---

# Features Included

## Core Features

* Automatic File Organization
* File Type Detection
* Automatic Folder Creation
* Unknown File Handling
* Professional CLI Interface
* Organized Output Messages

## Advanced Features

* Duplicate File Detection
* MD5 Hash Checking
* Error Handling
* Activity Logging
* File Summary Report
* Custom Folder Path Input
* Smart Categorization
* Professional Structure

---

# Example Folder Output

```bash
Downloads/
│
├── Images/
├── Documents/
├── Videos/
├── Audio/
├── Archives/
├── Python Files/
├── Web Files/
├── Others/
├── Duplicates/
└── organizer_log.txt
```

---

# How To Run

```bash
python advanced_file_organizer_pro.py
```

---

# Example Console Output

```bash
[MOVED] image.jpg → Images
[MOVED] notes.pdf → Documents
[DUPLICATE] song.mp3 moved to Duplicates
[OTHERS] random.xyz → Others
```

---

# Recommended README Sections

* Project Overview
* Features
* Technologies Used
* Screenshots
* Folder Structure
* How To Run
* Future Enhancements
* Author Information

---

# Premium Professional Features To Make Project Stand Out

## AI Smart Suggestions

* Detect frequently downloaded file types
* Suggest personalized folder organization patterns
* Intelligent naming recommendations

## Advanced Analytics Dashboard

* Track number of files organized
* Generate category usage statistics
* Display storage consumption reports
* Weekly cleanup analytics

## Enterprise-Level Features

* Automatic backup before organizing
* Undo last organization operation
* File encryption support
* Password-protected sensitive folders
* Secure audit logging

## Productivity Enhancements

* Auto-organize Downloads folder every startup
* Schedule organization tasks automatically
* Real-time monitoring of incoming files
* Desktop notifications after completion

## Modern User Experience

* Animated terminal loading effects
* Progress bar visualization
* Colorful CLI output
* Interactive menu system
* Branded startup banner

## Resume/Interview Highlight Features

This project demonstrates:

* Automation scripting
* File system management
* Error handling
* Data hashing techniques
* Python modular programming
* Professional software structure
* Real-world productivity solution engineering
* Problem-solving and optimization skills

---

# Advanced Professional Add-On Code Snippets

## Colored Terminal Output

```python
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.GREEN + "Organization Completed Successfully!")
print(Fore.CYAN + "Advanced File Organizer Pro")
```

---

## Progress Bar Integration

```python
from tqdm import tqdm

for file in tqdm(files, desc="Organizing Files"):
    process_file(file)
```

---

## Automatic Backup Feature

```python
backup_folder = os.path.join(base_path, "Backup")

if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

shutil.copy(file_path, backup_folder)
```

---

## File Statistics Report

```python
print("\n===== FILE STATISTICS =====")
print(f"Images   : {image_count}")
print(f"Documents: {document_count}")
print(f"Videos   : {video_count}")
print(f"Audio    : {audio_count}")
```

---

## Professional README Badge Ideas

```md
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Automation](https://img.shields.io/badge/Automation-Advanced-success)
![Status](https://img.shields.io/badge/Project-Professional-orange)
![License](https://img.shields.io/badge/License-MIT-green)

- GUI Version with Tkinter
- Drag & Drop Support
- AI-Based Smart Categorization
- Auto Cloud Backup
- Multi-threading Optimization
- Desktop Notifications
- Database Integration
- Dark Mode GUI

---

# Best GitHub Repo Description

"Advanced File Organizer Pro is a professional Python automation tool that intelligently organizes files into categorized folders, detects duplicates, generates logs, and improves digital workspace management using automation and smart file handling techniques."

```
    
