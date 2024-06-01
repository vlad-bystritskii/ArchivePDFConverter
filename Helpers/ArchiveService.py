import os
import zipfile
import comicapi
import rarfile

class ArchiveService:
    supported_types = {'.zip', '.rar', '.cba'}

    def extract(self, archive_path, extract_to):
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)

        lower_archive_path = archive_path.lower()

        if lower_archive_path.endswith('.zip'):
            self._extract_zip(archive_path, extract_to)
        elif lower_archive_path.endswith('.rar'):
            self._extract_rar(archive_path, extract_to)
        elif lower_archive_path.endswith('.cba'):
            self._extract_cba(archive_path, extract_to)
        else:
            raise ValueError(f"Unsupported archive format: {archive_path}")

    def _extract_zip(self, archive_path, extract_to):
        try:
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            print(f"ZIP extraction completed successfully to {extract_to}")
        except zipfile.BadZipFile as e:
            print(f"ZIP extraction failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during ZIP extraction: {e}")

    def _extract_rar(self, archive_path, extract_to):
        try:
            with rarfile.RarFile(archive_path, 'r') as rar_ref:
                rar_ref.extractall(extract_to)
            print(f"RAR extraction completed successfully to {extract_to}")
        except rarfile.BadRarFile as e:
            print(f"RAR extraction failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during RAR extraction: {e}")

    def _extract_cba(self, archive_path, extract_to):
        try:
            ca = comicapi.ComicArchive(archive_path)
            if ca.seemsToBeAComicArchive():
                ca.extract(extract_to)
                print(f"CBA extraction completed successfully to {extract_to}")
            else:
                print(f"The file {archive_path} does not appear to be a valid CBA archive")
        except Exception as e:
            print(f"An unexpected error occurred during CBA extraction: {e}")
