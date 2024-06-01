from Helpers.UnarchiveService import UnarchiveService
import os

if __name__ == "__main__":
    archive_path = input("Enter the path to the archive: ").replace("\\ ", " ").strip()
    extract_to = input("Enter the path to extract to: ").replace("\\ ", " ").strip()

    # Normalize paths to handle any escape characters and spaces
    archive_path = os.path.normpath(archive_path)
    extract_to = os.path.normpath(extract_to)

    service = UnarchiveService()
    try:
        service.extract(archive_path, extract_to)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
