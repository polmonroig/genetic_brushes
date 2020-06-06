from genetic.genetic import Genetic
import sys

REQUIRED_ARGS = 2


def usage():
    print("Wrong args")
    exit(1)


def main():
    # parse arguments
    if len(sys.argv) < REQUIRED_ARGS:
        usage()
    print('Starting application...')
    image_file = sys.argv[1]
    gen = Genetic(image_file)


if __name__ == '__main__':
    main()
