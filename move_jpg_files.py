import os
import shutil

# --- Folder paths ---
source_folder = r"soumya_task\MOVE_JPG_FILES\Pictures\source_images"     # Folder with .jpg files
destination_folder = r"soumya_task\MOVE_JPG_FILES\Pictures\moved_images" # Folder to move files to

# --- Create destination folder if not exists ---
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"📁 Created folder: {destination_folder}")

# --- Move all .jpg files ---
files_moved = 0
for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
        files_moved += 1
        print(f"✅ Moved: {file_name}")

# --- Summary ---
if files_moved == 0:
    print("⚠️ No .jpg files found in the source folder.")
else:
    print(f"\n🎯 Task Complete! {files_moved} .jpg files moved successfully.")
