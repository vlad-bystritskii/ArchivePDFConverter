# Archive to PDF Converter

# Overview
This project provides a comprehensive tool for extracting archives and creating PDFs from image files.
The primary goal is to support multiple archive formats, clean the extracted files, and compile images into PDFs while adding metadata and ensuring file size constraints.

## Supported Formats

- Archive Formats:
  - ZIP (.zip)
  - RAR (.rar)
  - Comic Book Archive (.cba)
- Image Formats for PDF:
  - PNG (.png)
  - JPEG (.jpg, .jpeg)

## Features

- Convert multiple image formats (e.g., JPG, PNG, BMP) to a single PDF file.
- Automatically handle image scaling and positioning.
- Easy-to-use command line interface.

## Requirements

- Python 3.6 or higher
- pip (Python package installer)

## Setup

To set up the environment and install the required dependencies, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/vlad-bystritskii/mangaPDFConverter.git
    cd mangaPDFConverter
    ```

2. Prepare the virtual environment and install dependencies using `make`:
    ```bash
    make prepare-env
    ```

## Usage

To convert images to PDF, place your images in the `images` directory and run the following command:

```bash
python main.py
```

The resulting PDF file will be saved in the `output` directory.

## Makefile Commands

The provided `Makefile` includes several commands to simplify the setup and usage process:

- `prepare-env`: Creates a virtual environment and installs all required dependencies from `requirements.txt`.
    ```bash
    make prepare-env
    ```

## Project Structure

- `images/`: Directory where you should place the images you want to convert to PDF.
- `output/`: Directory where the resulting PDF file will be saved.
- `requirements.txt`: File containing the list of dependencies needed for the project.
- `Makefile`: File containing commands for setting up the environment and converting images to PDF.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
