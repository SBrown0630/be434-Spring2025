#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-02-17
Purpose: Tetranucleotide frequency
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='str',
                        help='Input DNA sequence')

    return parser.parse_args()

# --------------------------------------------------

def main():
    """Make a jazz noise here"""
             
    args = get_args()
    DNA = args.DNA
    for char in DNA:
        count_a = DNA.count('A')
        count_c = DNA.count('C')
        count_g = DNA.count('G')
        count_t = DNA.count('T')

    print(count_a, count_c, count_g, count_t)


# --------------------------------------------------
if __name__ == '__main__':
    main()
