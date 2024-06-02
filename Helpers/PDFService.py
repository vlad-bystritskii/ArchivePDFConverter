import os
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
from Models.Folder import Folder
from Extensions.StringCleanPath import clean_path

class PDFService:
    image_supported_formats = {'.png', '.jpg', '.jpeg'}
    max_pdf_size = 195 * 1024 * 1024  # 195 MB

    def __init__(self, base_path: str, author: str):
        self.base_path = base_path
        self.author = author

    def create_pdfs(self, folder: Folder, extract_to):
        for subfolder in folder.subfolders:
            self.create_pdfs(subfolder, extract_to)
        
        images = [os.path.join(self.base_path, clean_path(element.path)) 
                  for element in folder.elements 
                  if any(element.path.lower().endswith(ext) for ext in PDFService.image_supported_formats)]
        
        if images:
            # Сортируем изображения по имени
            images.sort()

            relative_path = clean_path(folder.path)
            pdf_name = os.path.basename(relative_path) + ".pdf"
            destination_folder = os.path.join(extract_to, os.path.dirname(relative_path))
            
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            pdf_path = os.path.join(destination_folder, pdf_name)
            self._create_pdf(images, pdf_path)

    def _create_pdf(self, images, pdf_path):
        try:
            image_objs = [Image.open(img).convert('RGB') for img in images]
            image_objs[0].save(pdf_path, save_all=True, append_images=image_objs[1:])
            print(f"PDF created successfully at {pdf_path}")
            self._add_author_metadata(pdf_path)
            self._split_large_pdf(pdf_path)
        except Exception as e:
            print(f"An unexpected error occurred while creating PDF: {e}")

    def _add_author_metadata(self, pdf_path):
        try:
            pdf_reader = PdfReader(pdf_path)
            pdf_writer = PdfWriter()
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
            pdf_writer.add_metadata({
                '/Author': self.author
            })
            with open(pdf_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
            print(f"Author metadata added to {pdf_path}")
        except Exception as e:
            print(f"An unexpected error occurred while adding author metadata to {pdf_path}: {e}")

    def _split_large_pdf(self, pdf_path):
        if os.path.getsize(pdf_path) > PDFService.max_pdf_size:
            pdf_reader = PdfReader(pdf_path)
            part = 1
            pdf_writer = PdfWriter()
            current_size = 0

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
                temp_pdf_path = f"{pdf_path[:-4]}_temp.pdf"
                with open(temp_pdf_path, 'wb') as temp_pdf_file:
                    pdf_writer.write(temp_pdf_file)
                
                current_size = os.path.getsize(temp_pdf_path)
                if current_size > PDFService.max_pdf_size:
                    new_pdf_path = pdf_path.replace(".pdf", f" - Part {part}.pdf")
                    with open(new_pdf_path, 'wb') as output_pdf:
                        pdf_writer.write(output_pdf)
                    print(f"PDF split part created at {new_pdf_path}")
                    part += 1
                    pdf_writer = PdfWriter()
                os.remove(temp_pdf_path)

            if pdf_writer.pages:
                new_pdf_path = pdf_path.replace(".pdf", f" - Part {part}.pdf")
                with open(new_pdf_path, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)
                print(f"PDF split part created at {new_pdf_path}")

            os.remove(pdf_path)
            print(f"Original large PDF {pdf_path} removed")
