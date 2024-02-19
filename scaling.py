from PIL import Image
import argparse

def scale_and_compress_image(input_path, output_path, scale_factor=0.2, quality=85):
    original_image = Image.open(input_path)
    original_width, original_height = original_image.size
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    scaled_image = original_image.resize((new_width, new_height))
    scaled_image.save(output_path, quality=quality)

def main():
    parser = argparse.ArgumentParser(description="Scale and compress an image.")
    parser.add_argument("input_image", help="Path to the input image")
    parser.add_argument("output_image", help="Path to save the output image")
    parser.add_argument("--scale_factor", type=float, default=0.2, help="Scale factor for resizing (default: 0.2)")
    parser.add_argument("--quality", type=int, default=85, help="Compression quality (0-100, default: 85)")

    args = parser.parse_args()

    input_image_path = args.input_image
    output_image_path = args.output_image
    scale_factor = args.scale_factor
    compression_quality = args.quality

    scale_and_compress_image(input_image_path, output_image_path, scale_factor, compression_quality)
    print("Image scaled and compressed successfully.")

if __name__ == "__main__":
    main()
