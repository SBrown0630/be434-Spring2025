#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-03-15
Purpose: Print the reverse complement of DNA
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='str',
                        help='Input sequence or file')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.DNA
    if os.path.isfile(dna):
        dna = open(dna).read().strip()

    complement = str.maketrans('ACGTacgt', 'TGCAtgca')
    complemented_dna = dna.translate(complement)
    complemented_dna_list = list(complemented_dna)
    complemented_dna_list.reverse()
    print(''.join(complemented_dna_list))

# --------------------------------------------------
if __name__ == '__main__':
    main()
