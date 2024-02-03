
import os, math

def main():
    username = os.getlogin()
    return username

def find_recent_version(macro_prefix, folder_path):
    versions = []
    
    for root, dirs, files in os.walk(folder_path):
        for dir_name in dirs:
            full_path = os.path.join(root, dir_name)
            print(f"Checking folder: {full_path}")

            if dir_name.startswith(macro_prefix):
                version = dir_name[len(macro_prefix):].strip()
                
                versions.append(version)
    
    if versions:
        return max(versions)
    else:
        return None

def makeFolderPath():
    winUsername = main()
    str1 = "C:\\Users\\"
    str2 = "\\Downloads"

    folderPath = str1 + winUsername + str2
    return folderPath

# Example usage
macro_prefix = "Natro Macro"
folder_path = makeFolderPath()  # Replace with the actual path
recent_version = find_recent_version(macro_prefix, folder_path)

if recent_version:
    print(f"The most recent version of {macro_prefix} is {recent_version}")
else:
    print(f"No versions found for {macro_prefix}")

find_recent_version("Natro Macro", folder_path)
