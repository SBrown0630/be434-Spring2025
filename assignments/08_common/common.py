#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-04-23
Purpose: Find common words
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('FILE2',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file 2')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()


                    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
                    
    words1 = get_words(args.FILE1)
    words2 = get_words(args.FILE2)

    args.FILE1.close()
    args.FILE2.close()

    common = sorted(set(words1) & set(words2))

    for word in common:
        print(word, file=args.outfile)

    if args.outfile is not sys.stdout:
        args.outfile.close()

# --------------------------------------------------
def get_words(file):
    """Get words from file"""
    words = []
                    
    for line in file:
        words.extend(line.split())

    return words


# --------------------------------------------------
if __name__ == '__main__':
    main()
