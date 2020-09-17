import argparse

from image_list import create_image_list
from square_collage import create_square_image_collage


def create_collage(target, source, image_size, indent=0, recursive=False):
    """Create and save collage."""

    print("Scanning for images...")
    images = create_image_list(source, recursive)
    print(f"{len(images)} images found.")

    if images:
        print("Generating collage...")
        collage = create_square_image_collage(images, image_size, indent)
        print("Saving collage...")
        collage.save(target, dpi=(150, 150))
        print(f"Collage saved as {target!r}.")
    else:
        print("No images found.")


parser = argparse.ArgumentParser()
parser.add_argument("target", help="Collage file name.")
parser.add_argument("source", help="The source directory.")
parser.add_argument("-s", "--size", type=int, default=200,
                    help="Image tile size in px.")
parser.add_argument("-i", "--indent", type=int, default=0, nargs="?", const="5",
                    help="Indent size in px.")
parser.add_argument("-r", "--recursive", action="store_true", default=False,
                    help="Search for images recursively.")

args = parser.parse_args()

create_collage(args.target, args.source,
               image_size=args.size, indent=args.indent, recursive=args.recursive)
