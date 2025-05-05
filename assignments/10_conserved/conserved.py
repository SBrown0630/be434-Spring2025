#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-05-05
Purpose: Find conserved bases
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seqs = [line.strip() for line in args.FILE]
    for seq in seqs:
        print(seq)

    conserved = []
                    
    for i in range(len(seqs[0])):
        bases = [seq[i] for seq in seqs]
        if all(base == bases[0] for base in bases):
            conserved.append('|')
        else:
            conserved.append('X')

    print(''.join(conserved))

# --------------------------------------------------
if __name__ == '__main__':
    main()
