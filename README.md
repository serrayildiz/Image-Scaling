 # Image Scaling and Compression

This Python script is designed to scale and compress images efficiently. It's particularly useful for resizing large images or reducing their file size while maintaining acceptable quality.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Requirements](#requirements)
  - [Instructions](#instructions)
  - [Arguments](#arguments)
  - [Example](#example)


## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/serrayildiz/image-scaling-compression.git
    ```

2. Navigate to the project directory:

    ```sh
    cd image-scaling-compression
    ```

## Usage

### Requirements

- Python 3.x
- PIL (Python Imaging Library)

### Instructions

1. Ensure you have Python installed on your system. If not, you can download it from [python.org](https://www.python.org/downloads/).

2. Install the required PIL library:

    ```sh
    pip install pillow
    ```

3. Run the script with the desired parameters:

    ```sh
    python scale_and_compress.py input_image_path output_image_path --scale_factor 0.2 --quality 85
    ```

### Arguments

- `input_image_path`: Path to the input image file.
- `output_image_path`: Path to save the output scaled and compressed image.
- `--scale_factor`: Scale factor for resizing (default: 0.2).
- `--quality`: Compression quality (0-100, default: 85).

### Example

```sh
python scale_and_compress.py input_image.jpg output_image.jpg --scale_factor 0.2 --quality 85

