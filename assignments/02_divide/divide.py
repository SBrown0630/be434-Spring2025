#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-02-14
Purpose: Divide two numbers
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Divide two numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar='INT',
                        nargs=2,
                        type=int,
                        help='Numbers to divide')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numbers = args.numbers

    
    if numbers[1] == 0:
        print(f'usage: {sys.argv[0]} [-h] INT INT\nCannot divide by zero, dum-dum!', file=sys.stderr)
        sys.exit(1)
    else:
        divided = numbers[0] // numbers[1]
        print(f'{numbers[0]} / {numbers[1]} = {divided}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
