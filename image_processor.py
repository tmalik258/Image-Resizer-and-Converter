from PIL import Image as PillowImage
import os
import argparse


def image_resize_process(image_path, output_format="webp", quality=95):
    img = PillowImage.open(image_path)

    # Convert RGBA to RGB if necessary (for formats that don't support transparency)
    if output_format.upper() in ["JPG", "JPEG"] and img.mode in ("RGBA", "LA", "P"):
        # Create a white background
        background = PillowImage.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        background.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
        img = background

    # Resize image
    output_size = (5000, 5000)
    img.thumbnail(output_size)

    # Get the image filename without the extension
    image_file_name, image_extension = os.path.splitext(image_path)
    # Handle both Windows and Unix path separators
    if "original\\" in image_file_name:
        image_file_name = image_file_name.split("original\\")[1]
    elif "original/" in image_file_name:
        image_file_name = image_file_name.split("original/")[1]

    # Create resized directory if it doesn't exist
    os.makedirs("resized", exist_ok=True)

    # Normalize format name for file extension
    format_ext = output_format.lower()
    if format_ext == "jpg":
        format_ext = "jpeg"

    filename = f"resized/{image_file_name}.{output_format.lower()}"

    # Save the resized image with quality settings based on format
    if format_ext in ["jpeg", "jpg", "webp"]:
        # Quality range: 1-100 (1 = lowest quality, 100 = highest quality)
        if format_ext == "webp":
            # WebP also supports method parameter (0-6, higher = slower but better compression)
            img.save(filename, format=format_ext.upper(), quality=quality, method=6)
        else:
            img.save(filename, format=format_ext.upper(), quality=quality)
    elif format_ext == "png":
        # PNG uses optimize and compress_level (0-9, 0 = no compression, 9 = max compression)
        # Higher compression = lower file size, but PNG is lossless
        # Convert quality (1-100) to compress_level (0-9) inversely
        # High quality (100) = low compression (0), Low quality (1) = high compression (9)
        compress_level = 9 - int((quality / 100) * 9)
        img.save(filename, format=format_ext.upper(), optimize=True, compress_level=compress_level)
    else:
        # Default save for other formats
        img.save(filename, format=format_ext.upper())

    return filename


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Resize images from the 'original' directory"
    )

    # Create mutually exclusive group for format flags
    format_group = parser.add_mutually_exclusive_group()
    format_group.add_argument("--webp", action="store_const", const="webp", dest="format",
                             help="Convert images to WebP format (default)")
    format_group.add_argument("--png", action="store_const", const="png", dest="format",
                             help="Convert images to PNG format")
    format_group.add_argument("--jpg", action="store_const", const="jpg", dest="format",
                             help="Convert images to JPG format")
    format_group.add_argument("--jpeg", action="store_const", const="jpeg", dest="format",
                             help="Convert images to JPEG format")

    # Quality argument (1-100 recommended, default: 95)
    # Note: Values above 100 may be clamped to 100 by the image format
    parser.add_argument("--quality", "-q", type=int, default=95,
                       metavar="VALUE",
                       help="Image quality value (1-100 recommended, higher values may be clamped). Default: 95")

    parser.set_defaults(format="webp")

    return parser.parse_args()


# Example usage
if __name__ == "__main__":
    args = parse_arguments()

    # Validate quality value
    if args.quality < 1:
        print(f"Error: Quality value must be at least 1. Got: {args.quality}")
        exit(1)

    # Warn if quality is above 100 (most formats clamp to 100)
    if args.quality > 100:
        print(f"Warning: Quality value {args.quality} is above 100. Most image formats will clamp this to 100.")

    # Directory where the original images are stored
    original_dir = "original"

    # Check if directory exists
    if not os.path.exists(original_dir):
        print(f"Error: Directory '{original_dir}' does not exist!")
        exit(1)

    # List all files in the directory
    image_files = [f for f in os.listdir(original_dir)
                   if os.path.isfile(os.path.join(original_dir, f))]

    if not image_files:
        print(f"No files found in '{original_dir}' directory!")
        exit(1)

    print(f"Processing {len(image_files)} image(s) to {args.format.upper()} format with quality {args.quality}...")

    # Process each image in the directory
    for image_file in image_files:
        # Get the full file path
        image_file_path = os.path.join(original_dir, image_file)

        try:
            # Call the function to resize and save the image
            new_filename = image_resize_process(image_file_path, args.format, args.quality)
            print(f"The resized and saved image file: {new_filename}")
        except Exception as e:
            print(f"Error processing {image_file}: {str(e)}")
