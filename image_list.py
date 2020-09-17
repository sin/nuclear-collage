from pathlib import Path


def create_image_list(path_str, recursive=True):
    """Build a list of image paths (nonrecursive by default)."""

    path = Path(path_str)
    files = []

    for element in path.iterdir():

        if element.is_file() and element.suffix == '.jpg':
            abs_path = str(element.absolute())
            files.append(abs_path)

        if element.is_dir() and recursive == True:
            new_path = path_str + '/' + element.name
            sub_list = create_image_list(new_path)
            files.extend(sub_list)

    return files
