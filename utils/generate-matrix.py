"""Generate the matrix for each job of the build pipeline."""
import json
import argparse
from datetime import datetime


def generate_matrix(versions, input_image, output_image, gpu_options, version_prefix):
    """
    Generate the build matrix for the given versions and options.

    Args:
        versions (list): A list of version strings (Python or R versions).
        input_image (str): The base image name.
        output_image (str): The output image name.
        gpu_options (list): A list of booleans indicating whether to build GPU-enabled images.
        version_prefix (str): A prefix to denote the language version ("py" or "r").

    Returns:
        list: A list of dictionaries, each representing a build configuration.
    """
    matrix = []
    for version in versions:
        base = f"{input_image}:latest" if input_image == "base" else f"{input_image}:{version_prefix}{version}"
        output = f"{output_image}:{version_prefix}{version}"
        language_key = "java_version" if version_prefix == "py" else "r_version"
        version_entry = {"base_image_tag": f"{DH_ORGA}/{args.images_prefix}-{base}",
                         "output_image_main_tag": f"{DH_ORGA}/{args.images_prefix}-{output}",
                         language_key: version}
        for gpu in gpu_options:
            final_entry = version_entry.copy()
            suffix_gpu = "-gpu" if gpu else ""
            final_entry["base_image_tag"] += suffix_gpu
            final_entry["output_image_main_tag"] += suffix_gpu
            final_entry["output_image_tags"] = f'{final_entry["output_image_main_tag"]},{final_entry["output_image_main_tag"]}-{TODAY_DATE}'
            matrix.append(final_entry)
    return matrix


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_image", type=str)
    parser.add_argument("--output_image", type=str)
    parser.add_argument("--java_version_1", type=str, nargs="?", const="")
    parser.add_argument("--javav_version_2", type=str, nargs="?", const="")
    parser.add_argument("--javav_version_3", type=str, nargs="?", const="")
    parser.add_argument("--build_gpu", type=str, nargs="?")
    parser.add_argument("--base_image_gpu", type=str, nargs="?", const="")
    parser.add_argument("--dh_orga", type=str)
    parser.add_argument("--images_prefix", type=str)

    args = parser.parse_args()
    java_versions = [version for version in [args.java_version_1, args.java_version_2, args.java_version_3]
                       if version]
    gpu_options = [False, True] if args.build_gpu == "true" else [False]

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
            },
            {
                "base_image_tag": args.base_image_gpu,
                "output_image_main_tag": f"{DH_ORGA}/{onyxia_base_tag}-gpu",
                "output_image_tags": f"{DH_ORGA}/{onyxia_base_tag}-gpu,{DH_ORGA}/{onyxia_base_tag}-gpu-{TODAY_DATE}"
            }
            ]
    else:
        # Subsequent images, with versioning
        if java_versions:
            matrix = generate_matrix(java_versions, args.input_image, args.output_image,
                                     gpu_options, "py")

    matrix_json = json.dumps(matrix)
    print(matrix_json)
