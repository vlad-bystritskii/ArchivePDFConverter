import os
from typing import List, Dict
from Models.Folder import Folder
from Models.File import File
from Extensions.string_clean_path import clean_path
from Helpers.ArchiveService import ArchiveService

class FileManager:
    @staticmethod
    def build_repository_map(base_path: str, current_path: str = None) -> Folder:
        if current_path is None:
            current_path = base_path

        relative_path = os.path.relpath(current_path, base_path)
        folder = Folder(path=clean_path(relative_path))

        with os.scandir(current_path) as it:
            for entry in it:
                if entry.is_dir():
                    subfolder = FileManager.build_repository_map(base_path, entry.path)
                    if subfolder.subfolders or subfolder.elements:
                        folder.add_subfolder(subfolder)
                elif entry.is_file():
                    if any(entry.name.lower().endswith(ext) for ext in ArchiveService.supported_types):
                        element_path = os.path.relpath(entry.path, base_path)
                        element = File(path=clean_path(element_path))
                        folder.add_element(element)

        return folder

    @staticmethod
    def create_repository_map(path: str) -> Dict:
        repository_map = FileManager.build_repository_map(path)
        return repository_map.to_dict()
