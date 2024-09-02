import sys
from PIL import Image, ImageOps

def main():
    # Check the number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    # Check file extensions
    valid_extensions = (".jpg", ".jpeg", ".png")
    if not (input_image_path.lower().endswith(valid_extensions) and output_image_path.lower().endswith(valid_extensions)):
        sys.exit("Invalid input or output extension")

    if not input_image_path.split('.')[-1].lower() == output_image_path.split('.')[-1].lower():
        sys.exit("Input and output have different extensions")

    # Check if the input file exists
    try:
        input_image = Image.open(input_image_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Open the shirt image
    shirt_image = Image.open("shirt.png")

    # Resize and crop the input image to the same size as the shirt image
    input_image = ImageOps.fit(input_image, shirt_image.size)

    # Overlay the shirt image on the input image
    input_image.paste(shirt_image, shirt_image)

    # Save the resulting image
    input_image.save(sys.argv[2])

if __name__ == "__main__":
    main()
