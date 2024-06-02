import os
from Helpers.ArchiveService import ArchiveService
from Extensions.StringCleanPath import clean_path

def remove_extension(filename):
    return os.path.splitext(filename)[0]

def extract_archives(repository_map, base_path, extract_to):
    service = ArchiveService()
    for folder in repository_map.get("subfolders", []):
        extract_archives(folder, base_path, extract_to)
    for element in repository_map.get("elements", []):
        archive_path = os.path.join(base_path, clean_path(element["path"]))
        relative_path = clean_path(element["path"])
        destination_folder = os.path.join(extract_to, remove_extension(relative_path))
        
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
