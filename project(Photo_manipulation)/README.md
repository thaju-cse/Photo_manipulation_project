# Basic Image Duplication as Cinematic, black & white and drawing modes.

#### Video Demo:  https://drive.google.com/file/d/1RekXy2GaJ9p9RJgrAP9ifqASNWfpq1Je/view?usp=drive_link
#### Description:

    This project provides a 3 utilities for image processing using Python. It includes functions to apply cinematic effects, convert images to black and white, and transform images to look like pencil drawings. Additionally, it includes test cases for these functions to ensure they work correctly and consistently. The project also includes a script for copying files from my drive to codespace and utilities for working with timestamps and creating directories. This project aims to offer simple yet powerful tools for various image manipulation tasks and file system operations.

#### Project Structure:

    project.py: Contains functions for applying different effects to images.

    test_project.py: Contains test cases for the image processing functions using the unittest framework.

    README.md: Documentation for the project.


#### Detailed Description:

**project.py**:    This module contains the core image processing functions:

    cinematic(image_path, output_path):
        '''Enhances the contrast of the image and adds a slight tint to give it a      cinematic look.'''

    Usage:
        cinematic('input.jpg', 'output.jpg')

    bw(image_path, output_path):
        '''Converts the given image to black and white.'''

    drawing(image_path, output_path):
            '''Converts the image to look like a pencil drawing.'''

    Parameters:
        image_path: Path to the input image.
        output_path: Path where the output image will be saved, automatically it saved in seperate folder.
    Usage:
        cinematic('input.jpg', 'output.jpg')
        bw(image_path, output_path)
        drawing('input.jpg', 'output.jpg')

**test_project.py:**
    This module contains test cases for the functions defined in photo_effects.py using the unittest framework. It ensures that the image processing functions create the expected output files:

    testcinematic_effect: Tests the cinematic effect function on a set of images.

    test_bw(): Tests the black and white conversion function on a set of images.

    test_drawing(): Tests the drawing effect function on a set of images.

_Libraries required:_ pip install pillow

**Used advanced technologies for doubts:** ChatGpt
**Conclusion:**
    This project provides a versatile toolkit for basic image processing tasks and file system operations, wrapped in an easy-to-use Python package. With robust testing and clear separation of functionalities, it is designed to be extendable and maintainable.

Thank you.






