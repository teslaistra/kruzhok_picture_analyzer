#!/usr/bin/env python3

import argparse
import sys

import algorithms

parser = argparse.ArgumentParser(description='Process image to find KRUZHOK logo')
parser.add_argument('image', metavar='image', type=str,
                    help='image to process')
parser.add_argument('-t', '--template', metavar='template', type=str, default="logo.jpg",
                    help='image to process')
parser.add_argument('-a', '--algorithm', metavar="algorithm", type=str, default="OBR",
                    help='algorithm to use')
parser.add_argument('--debug', action='store_true')

available_algorithms = {"OBR": algorithms.obr.check,
                        "AKAZE": algorithms.akaze.check,
                        "BRISK": algorithms.brisk.check
                        }


def main():
    args = parser.parse_args(sys.argv[1:])
    image_path = args.image
    logo_path = args.template
    algorithm = available_algorithms.setdefault(args.algorithm, available_algorithms["OBR"])
    result = algorithm(logo_path, image_path, args.debug)
    if result:
        print("kruzhok")
    return result


if __name__ == "__main__":
    main()
