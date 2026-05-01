import os

print("Batch File Renamer")

path = input("Enter folder path: ")

if not os.path.exists(path):
    print("Invalid path!")
    exit()

files = os.listdir(path)

count = 1

for file in files:
    old_path = os.path.join(path, file)

    if os.path.isdir(old_path):
        continue

    name, ext = os.path.splitext(file)

    new_name = f"file_{count}{ext}"
    new_path = os.path.join(path, new_name)

    os.rename(old_path, new_path)
    print(f"{file} → {new_name}")

    count += 1

print("\nRenaming completed!")