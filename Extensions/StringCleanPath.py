def clean_path(path: str) -> str:
    return path.replace("\\", "").replace("/ -", "").strip()