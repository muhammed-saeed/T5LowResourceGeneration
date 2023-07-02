import os
# Recursive function to get all files inside a folder and its subfolders
def get_all_files(folder_path):
    file_paths = []
    for root, directories, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

def writelines(folder_path, lines):
    with open(folder_path, "w") as fb:
        fb.writelines(lines)
    print(f"Complete the writing to the file {folder_path}")



def folderchecker(folder_path_pcm, folder_list):
    folder_path = os.path.join(folder_path_pcm, *folder_list[:-1])
    print(folder_path)

    # Create the folder path if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    print("Folder created:", folder_path)

    file_path = os.path.join(folder_path, folder_list[-1])
    if not os.path.exists(file_path):
        # Create the file
        with open(file_path, "w") as file:
            print("File created:", file_path)

    return file_path

