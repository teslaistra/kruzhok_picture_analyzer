#!/usr/bin/env python3

import argparse
import sys
import algorithms

available_algorithms = {"OBR": algorithms.obr.check,
                        "AKAZE": algorithms.akaze.check,
                        "BRISK": algorithms.brisk.check
                        }

parser = argparse.ArgumentParser(description='Process image to find KRUZHOK logo')
parser.add_argument('image', metavar='image', type=str,
                    help='image to process')
parser.add_argument('-a', '--algorithm', metavar="algorithm", type=str, default="OBR",
                    help='algorithm to use')


def main():
    args = parser.parse_args(sys.argv[1:])
    image_path = args.image
    algorithm = available_algorithms.setdefault(args.algorithm, available_algorithms["OBR"])
    algorithm(image_path)


if __name__ == "__main__":
    main()
