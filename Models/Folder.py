from typing import List, Dict
from Models.File import File

class Folder:
    def __init__(self, path: str):
        self.path = path
        self.subfolders: List['Folder'] = []
        self.elements: List[File] = []

    def add_subfolder(self, folder: 'Folder'):
        self.subfolders.append(folder)

    def add_element(self, element: File):
        self.elements.append(element)

    def to_dict(self) -> Dict:
        return {
            "path": self.path,
            "subfolders": [subfolder.to_dict() for subfolder in self.subfolders],
            "elements": [element.to_dict() for element in self.elements]
        }
