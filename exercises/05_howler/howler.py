#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-03-15
Purpose: Howler Exercise
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler Exercise',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()
                    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
                    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
                    
    if args.outfile:
        print(args.text.upper(), file=open(args.outfile, 'wt'))
    else:
        print(args.text.upper())
# --------------------------------------------------
if __name__ == '__main__':
    main()
