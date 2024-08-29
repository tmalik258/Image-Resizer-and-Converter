from PIL import Image as PillowImage
from io import BytesIO
import os
import sys


def image_resize_process(image_path):
    img = PillowImage.open(image_path)

    # Resize image
    output_size = (1000, 1000)
    img.thumbnail(output_size)

    # Save the resized image to a BytesIO buffer
    output_buffer = BytesIO()
    img.save(output_buffer, format="png")
    output_buffer.seek(0)

    # Get the image filename without the extension
    image_file_name, image_extension = os.path.splitext(image_path)
    image_file_name = image_file_name.split("original_images\\")[1]
    filename = f"resized_images/{image_file_name}.webp"

    # Save the buffer content to the new image file
    with open(filename, "wb") as f:
        f.write(output_buffer.read())

    return filename


# Example usage
if __name__ == "__main__":
    # Directory where the original images are stored
    original_images_dir = "original_images"

    # List all files in the directory
    image_files = os.listdir(original_images_dir)

    # Process each image in the directory
    for image_file in image_files:
        # Get the full file path
        image_file_path = os.path.join(original_images_dir, image_file)

        # Call the function to resize and save the image
        new_filename = image_resize_process(image_file_path)
        print(f"The resized and saved image file: {new_filename}")
