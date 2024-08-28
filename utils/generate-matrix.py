"""Generate the matrix for each job of the build pipeline."""
import json
import argparse
from datetime import datetime


def generate_matrix(versions, input_image, output_image):
    """
    Generate the build matrix for the given versions and options.

    Args:
        versions (list): A list of version strings (Python or R versions).
        input_image (str): The base image name.
        output_image (str): The output image name.

    Returns:
        list: A list of dictionaries, each representing a build configuration.
    """
    matrix = []
    for version in versions:
        base = f"{input_image}:latest" if input_image == "base" else f"{input_image}:{version}"
        output = f"{output_image}:{version}"
        version_entry = {"base_image_tag": f"{DH_ORGA}/{args.images_prefix}-{base}",
                         "output_image_main_tag": f"{DH_ORGA}/{args.images_prefix}-{output}"}

        final_entry = version_entry.copy()
        final_entry["output_image_tags"] = f'{final_entry["output_image_main_tag"]},{final_entry["output_image_main_tag"]}-{TODAY_DATE}'
        matrix.append(final_entry)
    return matrix


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_image", type=str)
    parser.add_argument("--output_image", type=str)
    parser.add_argument("--java_version_1", type=str, nargs="?", const="")
    parser.add_argument("--java_version_2", type=str, nargs="?", const="")
    parser.add_argument("--java_version_3", type=str, nargs="?", const="")
    parser.add_argument("--dh_orga", type=str)
    parser.add_argument("--images_prefix", type=str)

    args = parser.parse_args()
    java_versions = [version for version in [args.java_version_1, args.java_version_2, args.java_version_3]
                       if version]

    DH_ORGA = args.dh_orga.lower()
    TODAY_DATE = datetime.today().strftime('%Y.%m.%d')

    if args.output_image == "base":
        # Building base onyxia image from external images
        onyxia_base_tag = f"{args.images_prefix}-base:latest"
        matrix = [
            {
                "base_image_tag": args.input_image,
                "output_image_main_tag": f"{DH_ORGA}/{onyxia_base_tag}",
                "output_image_tags": f"{DH_ORGA}/{onyxia_base_tag},{DH_ORGA}/{onyxia_base_tag}-{TODAY_DATE}"
            }
            ]
    else:
        # Subsequent images, with versioning
        if java_versions:
            matrix = generate_matrix(java_versions, args.input_image, args.output_image)

    matrix_json = json.dumps(matrix)
    print(matrix_json)
