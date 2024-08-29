# Simple Image Resizer and Extension Converter

This is a simple Python project that resizes images and converts them to `.webp` format by default. The project uses a virtual environment for managing dependencies and processes images placed in the `original_images` folder. The resized images will be stored in the `resized_images` folder.

## Features

- Resizes images to a default size of 1000x1000 pixels.
- Converts images to `.webp` format.
- The size and format can be easily customized in the script.

## Requirements

- Python 3.x

## Setup and Installation

1. **Clone the repository** and navigate to the project directory.

2. **Create a virtual environment**:
   
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Place your images** into the `original_images/` folder.

2. **Run the image processor**:

   ```bash
   python image_processor.py
   ```

3. **Check the `resized_images/` folder** to find your resized images, saved by default in the `.webp` format.

## Customization

You can customize the image size and format by modifying the following variables in the `image_processor.py` file:

- **Size**: Change the values in `output_size = (1000, 1000)` to set your desired image dimensions.
- **Format**: Modify `filename = f"resized_images/{image_file_name}.webp"` to change the output file format.
