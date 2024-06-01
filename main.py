from Helpers.ArchiveService import ArchiveService
from Helpers.FileManager import FileManager
from Extensions.string_clean_path import clean_path
import os
import json

def extract_archives(repository_map, base_path, extract_to):
    service = ArchiveService()
    for folder in repository_map.get("subfolders", []):
        extract_archives(folder, base_path, extract_to)
    for element in repository_map.get("elements", []):
        archive_path = os.path.join(base_path, clean_path(element["path"]))
        relative_path = os.path.dirname(clean_path(element["path"]))
        destination_folder = os.path.join(extract_to, relative_path)
        
        if not os.path.exists(destination_folder):
            try:
                os.makedirs(destination_folder)
            except OSError as e:
                print(f"Error creating directory {destination_folder}: {e}")
                continue
        
        try:
            service.extract(archive_path, destination_folder)
        except ValueError as e:
            print(f"ValueError for {archive_path}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {archive_path}: {e}")

if __name__ == "__main__":
    path_to_folder = clean_path(input("Enter the path to the folder: "))
    repository_map = FileManager.create_repository_map(path_to_folder)
    
    extract_to_folder = os.path.join(clean_path(path_to_folder), "Temporary")
    if not os.path.exists(extract_to_folder):
        try:
            os.makedirs(extract_to_folder)
        except OSError as e:
            print(f"Error creating directory {extract_to_folder}: {e}")
            sys.exit(1)

    extract_archives(repository_map, clean_path(path_to_folder), clean_path(extract_to_folder))
