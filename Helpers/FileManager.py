import os
from typing import List, Dict
from Models.Folder import Folder
from Models.File import File
from Extensions.StringCleanPath import clean_path
from Helpers.ArchiveService import ArchiveService

def build_repository_map(base_path: str) -> Folder:
    folder = Folder(path=clean_path(os.path.basename(base_path)))

    folder_dict = {clean_path(base_path): folder}

    for current_path, subdirs, files in os.walk(base_path):
        relative_path = clean_path(os.path.relpath(current_path, base_path))
        current_folder = folder_dict[clean_path(current_path)]

        for file in files:
            if any(file.lower().endswith(ext) for ext in ArchiveService.supported_types):
                element_path = clean_path(os.path.relpath(os.path.join(current_path, file), base_path))
                element = File(path=element_path)
                current_folder.add_element(element)

        for subdir in subdirs:
            subfolder_path = clean_path(os.path.join(relative_path, subdir))
            subfolder = Folder(path=subfolder_path)
            current_folder.add_subfolder(subfolder)
            folder_dict[clean_path(os.path.join(current_path, subdir))] = subfolder

    return folder

def create_repository_map(path: str) -> Dict:
    repository_map = build_repository_map(path)
    return repository_map.to_dict()