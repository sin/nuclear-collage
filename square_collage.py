from PIL import Image
import math
import numpy as np


def create_square_image_collage(images, image_size, indent):
    """Create square collage from list of images."""

    matrix_size = math.floor(math.sqrt(len(images)))
    max_images = matrix_size * matrix_size

    diff = len(images) - max_images
    if diff:
        print(f"Warning: {diff} images omitted.")

    images = images[0:max_images]
    images = np.array(images).reshape((matrix_size, matrix_size))

    collage_size = matrix_size * image_size + (matrix_size - 1) * indent
    collage_color = (255, 255, 255)
    collage = Image.new(mode='RGB', size=(
        collage_size, collage_size), color=collage_color)

    for i in range(matrix_size):
        for j in range(matrix_size):
            image = Image.open(images[i, j])
            image = image.resize((image_size, image_size),
                                 resample=Image.BICUBIC)
            collage.paste(image, box=(i * (image_size + indent),
                                      j * (image_size + indent)))

    return collage
