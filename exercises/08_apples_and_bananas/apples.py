#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-04-01
Purpose: Apples and bananas
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel',
                        metavar='str',
                        type=str,
                        choices='aeiou',
                        default='a')


    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
                        
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel

    new = ''
    for char in text:
        if char in 'aeiou':
            new += vowel
        elif char in 'AEIOU':
            new += vowel.upper()
        else:
            new += char
    print(new)
# --------------------------------------------------
if __name__ == '__main__':
    main()
