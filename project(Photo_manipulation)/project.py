from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import sys
import os


def main():
    if len(sys.argv) != 3:
        print("Usage: python photo_effects.py <effect> <input_image>")
        print("Effects: cinematic, bw, drawing")
        sys.exit(1)

    effect = sys.argv[1]
    input_image = 'Images/input/'+sys.argv[2]
    output_image = sys.argv[2]

    if not os.path.isfile(input_image):
        print(f"File not found: {input_image}")
        sys.exit(1)

    if effect == 'cinematic':
        cinematic(input_image, 'Images/cinematic/'+output_image)
    elif effect == 'bw':
        bw(input_image, 'Images/bw/'+output_image)
    elif effect == 'drawing':
        drawing(input_image, 'Images/drawing/'+output_image)
    else:
        print("Invalid effect. Choose from: cinematic, bw, drawing")
        sys.exit(1)


def cinematic(image_path, output_path):
    """
        Apply a cinematic effect to the image.
    """
    try:
        with Image.open(image_path) as img:
            # Increase contrast
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.5)

            # Add a slight tint
            tint_color = (230, 153, 153)
            tint_layer = Image.new('RGB', img.size, tint_color)
            img = Image.blend(img, tint_layer, 0.1)

            # Save the result
            img.save(output_path)
            print(f"Cinematic photo saved as {output_path}")
            return 1
    except:
        print("Something went wrong !!!")
        return 0


def bw(image_path, output_path):
    """
        Convert the image to black and white.
    """
    try:
        with Image.open(image_path) as img:
            # Convert image to black and white
            bw_image = img.convert('L')

            # Save the new image
            bw_image.save(output_path)
            print(f"Black and white photo saved as {output_path}")
            return 1
    except:
        print("Something went wrong !!!")
        return 0


def drawing(image_path, output_path):
    """
        Convert the image to look like a pencil drawing.
    """
    try:
        with Image.open(image_path) as img:
            # Convert to grayscale
            gray_image = img.convert('L')

            # Invert image
            inverted_image = ImageOps.invert(gray_image)

            # Blur the inverted image
            blurred_image = inverted_image.filter(ImageFilter.GaussianBlur(10))

            # Blend the original gray image with the blurred inverted image
            drawing_image = Image.blend(gray_image, blurred_image, 0.5)

            # Save the new image
            drawing_image.save(output_path)
            print(f"Drawing photo saved as {output_path}")
            return 1
    except:
        print("Something went wrong !!!")
        return 0


if __name__ == "__main__":
    main()
