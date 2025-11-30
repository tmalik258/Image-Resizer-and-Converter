# Simple Image Resizer and Extension Converter

This is a simple Python project that resizes images and converts them to `.webp` format by default. The project uses a virtual environment for managing dependencies and processes images placed in the `original` folder. The resized images will be stored in the `resized` folder.

## Features

- Resizes images to a maximum size of 5000x5000 pixels (maintains aspect ratio).
- Converts images to multiple formats: WebP (default), PNG, JPG, or JPEG.
- Adjustable image quality settings (1-100, default: 95).
- Automatic handling of transparency for JPG/JPEG formats (converts RGBA to RGB with white background).
- Command-line interface for easy customization.

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

1. **Place your images** into the `original/` folder.

2. **Run the image processor**:

   ```bash
   python image_processor.py
   ```

   By default, this will process all images in the `original/` folder and convert them to WebP format with quality 95.

3. **Check the `resized/` folder** to find your resized images, saved by default in the `.webp` format.

## Command-Line Options

The script supports several command-line arguments for customization:

- **Format selection** (mutually exclusive):
  - `--webp` - Convert images to WebP format (default)
  - `--png` - Convert images to PNG format
  - `--jpg` - Convert images to JPG format
  - `--jpeg` - Convert images to JPEG format

- **Quality setting**:
  - `--quality` or `-q` - Set image quality (1-100, default: 95)

### Examples

Convert to PNG format:

```bash
python image_processor.py --png
```

Convert to JPG with custom quality:

```bash
python image_processor.py --jpg --quality 85
```

Convert to WebP with highest quality:

```bash
python image_processor.py --webp -q 100
```

## Customization

- **Size**: To change the maximum output size, modify `output_size = (5000, 5000)` in the `image_resize_process` function within `image_processor.py`.
- **Format**: Use command-line arguments (`--webp`, `--png`, `--jpg`, `--jpeg`) to change the output format without editing the script.
- **Quality**: Use the `--quality` or `-q` argument to adjust image quality (1-100).
