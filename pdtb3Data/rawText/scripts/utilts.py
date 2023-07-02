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
    folder_path =  folder_path_pcm + '/'.join(folder_list)
    print(folder_path)

    # Check if the folder exists
    if not os.path.exists(folder_path):
        # Create the folder
        os.makedirs(folder_path)
        print("Folder created:", folder_path)
        return folder_path
    else:
        print("Folder already exists:", folder_path)
        return folder_path