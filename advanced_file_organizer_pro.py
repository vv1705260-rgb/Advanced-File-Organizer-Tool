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

    main()
