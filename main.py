from Helpers.FileManager import create_repository_map
from Extensions.StringCleanPath import clean_path
from Helpers.ArchiveExtractor import extract_archives
import os
import sys

if __name__ == "__main__":
    path_to_folder = clean_path(input("Enter the path to the folder: "))
    repository_map = create_repository_map(path_to_folder)
    
    extract_to_folder = os.path.join(clean_path(path_to_folder), "Temporary")
    if not os.path.exists(extract_to_folder):
        try:
            os.makedirs(extract_to_folder)
        except OSError as e:
            print(f"Error creating directory {extract_to_folder}: {e}")
            sys.exit(1)

    extract_archives(repository_map, clean_path(path_to_folder), clean_path(extract_to_folder))
