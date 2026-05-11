import os
import shutil
import time
from datetime import datetime

from config import FILE_CATEGORIES, LOG_FOLDER, LOG_FILE, REPORT_FILE
from banner import show_banner
from utils import create_folder, format_size

# Show Banner
show_banner()

# User Input
path = input("\nEnter folder path to organize: ")

# Check Folder
if not os.path.exists(path):
    print("\n❌ Folder does not exist!")
    exit()

# Create Logs Folder
create_folder(LOG_FOLDER)

# Statistics
total_files = 0
moved_files = 0
total_size = 0

# Start Time
start_time = time.time()

# Logging Function
def write_log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(message + "\n")

# Report File
report = open(REPORT_FILE, "w", encoding="utf-8")

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

write_log(f"\n===== ORGANIZER STARTED : {current_time} =====")

report.write("ADVANCED FILE ORGANIZER REPORT\n")
report.write("=" * 50 + "\n\n")

# Organizing Files
for file in os.listdir(path):

    file_path = os.path.join(path, file)

    if os.path.isdir(file_path):
        continue

    total_files += 1

    extension = os.path.splitext(file)[1].lower()

    file_size = os.path.getsize(file_path)
    total_size += file_size

    moved = False

    for category, extensions in FILE_CATEGORIES.items():

        if extension in extensions:

            category_folder = os.path.join(path, category)

            create_folder(category_folder)

            destination = os.path.join(category_folder, file)

            # Rename duplicate files
            if os.path.exists(destination):

                name = os.path.splitext(file)[0]
                new_name = f"{name}_{int(time.time())}{extension}"

                destination = os.path.join(category_folder, new_name)

            shutil.move(file_path, destination)

            print(f"✅ {file} → {category}")

            write_log(f"Moved: {file} --> {category}")

            report.write(f"{file} --> {category}\n")

            moved_files += 1
            moved = True
            break

    # Uncategorized Files
    if not moved:

        others_folder = os.path.join(path, "Others")

        create_folder(others_folder)

        shutil.move(file_path, os.path.join(others_folder, file))

        print(f"📂 {file} → Others")

        report.write(f"{file} --> Others\n")

        moved_files += 1

# End Time
end_time = time.time()

# Final Report
report.write("\n" + "=" * 50 + "\n")
report.write(f"Total Files : {total_files}\n")
report.write(f"Moved Files : {moved_files}\n")
report.write(f"Total Size  : {format_size(total_size)}\n")
report.write(f"Time Taken  : {round(end_time - start_time, 2)} sec\n")

report.close()

# Console Summary
print("\n" + "=" * 60)
print("         ORGANIZATION COMPLETED")
print("=" * 60)

print(f"📁 Total Files : {total_files}")
print(f"✅ Moved Files : {moved_files}")
print(f"💾 Total Size  : {format_size(total_size)}")
print(f"⏱️ Time Taken   : {round(end_time - start_time, 2)} sec")

print("\n📄 Report Generated : file_report.txt")
print("📄 Logs Saved Successfully")
print("\n🚀 Advanced File Organizer Finished!")
