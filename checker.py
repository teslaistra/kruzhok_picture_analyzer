#!/usr/bin/env python3

import argparse
import os
import sys

import algorithms

parser = argparse.ArgumentParser(description='Process image to find KRUZHOK logo')
parser.add_argument('image', metavar='image', type=str,
                    help='path/to/image to process')
parser.add_argument('-t', '--template', metavar='template', type=str, default="logo.jpg",
                    help='path/to/template to use as template (or folder with templates for "TEMPLATE" algorithm)')
parser.add_argument('-a', '--algorithm', metavar="algorithm", type=str, default="AKAZE",
                    help='algorithm to use ("ORB", "AKAZE" or "TEMPLATE")')
parser.add_argument('--debug', action='store_true', help='enables debugging logging')

available_algorithms = {
    "ORB": algorithms.orb.check,
    "AKAZE": algorithms.akaze.check,
    "TEMPLATE": algorithms.template.check
}


def main():
    args = parser.parse_args(sys.argv[1:])
    image_path = args.image
    logo_path = args.template
    algorithm = available_algorithms.setdefault(args.algorithm, available_algorithms["ORB"])

    if not os.path.isfile(image_path):
        print(f"\nThis file {image_path} doesn't exist!")
        return

    if algorithm == available_algorithms["TEMPLATE"] and not os.path.isdir(logo_path):
        print(f"\nThere is no template folder at {logo_path} ! Trying to get default template folder...")
        if os.path.isdir("./templates/"):
            logo_path = "./templates/"
            print(f"Will now use default template folder at {logo_path}: ", end="")
        else:
            print(f"There is no template folder at {logo_path} and no default template folder!")
            return
    elif algorithm != available_algorithms["TEMPLATE"] and not os.path.isfile(logo_path):
        print(f"\nThere is no template at {logo_path} ! Trying to get default template...")
        if os.path.isfile("logo.jpg"):
            logo_path = "./logo.jpg"
            print(f"Will now use default template at {logo_path}: ", end="")
        else:
            print(f"There is no template at {logo_path} and no default template!")
            return

    result = algorithm(logo_path, image_path, args.debug)
    if result:
        print("kruzhok")
    else:
        return


if __name__ == "__main__":
    main()
