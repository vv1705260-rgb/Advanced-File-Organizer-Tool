import os

# Create Folder Function
def create_folder(folder_path):

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# File Size Converter
def format_size(size):

    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} TB"
