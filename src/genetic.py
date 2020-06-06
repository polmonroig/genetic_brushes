from genetic.genetic import Genetic
from random import seed
import sys

REQUIRED_ARGS = 2


def usage():
    """
    Outputs program usage and exits
    :return: None
    """
    print("genetic: genetic image")
    print("image: image to generate")
    exit(1)


def main():
    # parse arguments
    if len(sys.argv) < REQUIRED_ARGS:
        usage()
    print('Starting brushing...')
    # seed(342)
    image_file = sys.argv[1]
    error_margin = 0.1
    gen = Genetic(image_file, error_margin)
    gen.start(10)


if __name__ == '__main__':
    main()
