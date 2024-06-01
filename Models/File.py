from typing import List, Dict

class File:
    def __init__(self, path: str):
        self.path = path

    def to_dict(self) -> Dict:
        return {"path": self.path}
