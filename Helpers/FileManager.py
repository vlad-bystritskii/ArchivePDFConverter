import os
from typing import List, Dict
from Models.Folder import Folder
from Models.File import File
from Extensions.StringCleanPath import clean_path
from Helpers.ArchiveService import ArchiveService

def build_repository_map(base_path: str) -> Folder:
    folder = Folder(path=clean_path(os.path.basename(base_path)))

    for current_path, subdirs, files in os.walk(base_path):
        relative_path = os.path.relpath(current_path, base_path)
        current_folder = Folder(path=clean_path(relative_path))

        for file in files:
            if any(file.lower().endswith(ext) for ext in ArchiveService.supported_types):
                element_path = os.path.relpath(os.path.join(current_path, file), base_path)
                element = File(path=clean_path(element_path))
                current_folder.add_element(element)

        for subdir in subdirs:
            subfolder_path = os.path.relpath(os.path.join(current_path, subdir), base_path)
            subfolder = Folder(path=clean_path(subfolder_path))
            current_folder.add_subfolder(subfolder)

        if current_folder.elements or current_folder.subfolders:
            folder.add_subfolder(current_folder)

    return folder

def create_repository_map(path: str) -> Dict:
    repository_map = build_repository_map(path)
    return repository_map.to_dict()
