import os
import shutil
import time
from datetime import datetime

# =========================
# ADVANCED FILE ORGANIZER
# =========================

print("=" * 50)
print("      ADVANCED FILE ORGANIZER TOOL")
print("=" * 50)

# User Input
path = input("\nEnter folder path to organize: ")

# Check Path Exists
if not os.path.exists(path):
    print("\n❌ Folder does not exist!")
    exit()

# File Categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".java", ".cpp", ".html", ".css", ".js"],
    "Archives": [".zip", ".rar"],
    "Applications": [".exe", ".msi"]
}

# Create Logs Folder
if not os.path.exists("logs"):
    os.makedirs("logs")

# Log File
log_file = "logs/organizer.log"

# Statistics
total_files = 0
moved_files = 0
skipped_files = 0

# Start Time
start_time = time.time()

# Write Logs
def write_log(message):
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(message + "\n")

# Current Time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

write_log(f"\n===== ORGANIZER STARTED : {current_time} =====")

# Organize Files
for file in os.listdir(path):

    file_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(file_path):
        skipped_files += 1
        continue

    total_files += 1
    moved = False

    # Extension
    extension = os.path.splitext(file)[1].lower()

    # Match Category
    for category, extensions in FILE_CATEGORIES.items():

        if extension in extensions:

            category_folder = os.path.join(path, category)

            # Create Folder
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            # Destination
            destination = os.path.join(category_folder, file)

            # Rename if duplicate exists
            if os.path.exists(destination):

                file_name = os.path.splitext(file)[0]
                new_name = f"{file_name}_{int(time.time())}{extension}"

                destination = os.path.join(category_folder, new_name)

            # Move File
            shutil.move(file_path, destination)

            print(f"✅ Moved: {file} → {category}")

            write_log(f"Moved: {file} --> {category}")

            moved_files += 1
            moved = True
            break

    # Uncategorized Files
    if not moved:

        others_folder = os.path.join(path, "Others")

        if not os.path.exists(others_folder):
            os.makedirs(others_folder)

        shutil.move(file_path, os.path.join(others_folder, file))

        print(f"📂 Moved: {file} → Others")

        write_log(f"Moved: {file} --> Others")

        moved_files += 1

# End Time
end_time = time.time()

# Summary
print("\n" + "=" * 50)
print("          ORGANIZATION COMPLETED")
print("=" * 50)

print(f"📁 Total Files Scanned : {total_files}")
print(f"✅ Files Organized     : {moved_files}")
print(f"⏭️ Skipped Folders      : {skipped_files}")
print(f"⏱️ Time Taken           : {round(end_time - start_time, 2)} seconds")

write_log(f"Total Files: {total_files}")
write_log(f"Moved Files: {moved_files}")
write_log("===== ORGANIZER FINISHED =====")

print("\n📄 Log file saved in logs/organizer.log")
print("🚀 Thank You For Using Advanced File Organizer!")
