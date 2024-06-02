from Helpers.PDFService import PDFService
from Helpers.FileManager import create_repository_map, build_image_repository_map, clean_empty_folders_and_non_images
from Extensions.StringCleanPath import clean_path
from Helpers.ArchiveExtractor import extract_archives
import os
import sys
import shutil

if __name__ == "__main__":
    path_to_folder = clean_path(input("Enter the path to the folder: "))
    author = input("Enter the author's name: ").strip()
    
    repository_map = create_repository_map(path_to_folder)
    
    extract_to_folder = os.path.join(clean_path(path_to_folder), "Temporary")
    if not os.path.exists(extract_to_folder):
        try:
            os.makedirs(extract_to_folder)
        except OSError as e:
            print(f"Error creating directory {extract_to_folder}: {e}")
            sys.exit(1)

    extract_archives(repository_map, clean_path(path_to_folder), clean_path(extract_to_folder))
    
    temp_repository_map = build_image_repository_map(extract_to_folder)
    
    clean_empty_folders_and_non_images(temp_repository_map)
    
    pdfs_folder = os.path.join(clean_path(path_to_folder), "PDFs")
    if not os.path.exists(pdfs_folder):
        try:
            os.makedirs(pdfs_folder)
        except OSError as e:
            print(f"Error creating directory {pdfs_folder}: {e}")
            sys.exit(1)
    
    pdf_service = PDFService(extract_to_folder, author)
    pdf_service.create_pdfs(temp_repository_map, clean_path(pdfs_folder))

    try:
        shutil.rmtree(extract_to_folder)
        print(f"Temporary folder {extract_to_folder} deleted successfully")
    except Exception as e:
        print(f"Error deleting Temporary folder {extract_to_folder}: {e}")