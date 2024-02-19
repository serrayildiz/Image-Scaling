from PIL import Image
import os

def scale_and_compress_image(input_path, output_path, scale_factor=0.2, quality=85):
    # Open the image
    original_image = Image.open(input_path)

    # Get the original size
    original_width, original_height = original_image.size

    # Calculate the new size based on the scale factor
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    # Resize the image
    scaled_image = original_image.resize((new_width, new_height))

    # Save the scaled image with compression
    scaled_image.save(output_path, quality=quality)

if __name__ == "__main__":
    # Set your input and output paths
    input_image_path = r"C:\Users\serra\OneDrive\Masaüstü\Yeni klasör\IMG_8482.jpeg"
    output_image_path = r"C:\Users\serra\OneDrive\Masaüstü\Yeni klasör\output.jpg"

    # Set the scale factor (e.g., 0.5 for 50% scaling)
    scale_factor = 0.2

    # Set the compression quality (0-100, 100 being the best quality)
    compression_quality = 85

    # Perform scaling and compression
    scale_and_compress_image(input_image_path, output_image_path, scale_factor, compression_quality)

    print("Image scaled and compressed successfully.")
