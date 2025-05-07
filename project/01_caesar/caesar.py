#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-05-07
Purpose: caesar shift
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    
    parser = argparse.ArgumentParser(
        description='caesar shift',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='std.out')

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.FILE.read()

    table = sub_table(args.number, args.decode)

    encoded = '\n'.join([caesar_shift(line, table) 
                for line in text.splitlines()])
    
    print(encoded, file=args.outfile)

    print(encoded)


# --------------------------------------------------
def sub_table(shift, decode=False):
    """Create a caesar substitution table"""

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted = alpha[shift:] + alpha[:shift]
    
    if decode:
        return str.maketrans(shifted, alpha)
    else:
        return str.maketrans(alpha, shifted)

# --------------------------------------------------
def caesar_shift(text, table):
    """Shift the text using the substitution table"""
    
    result = []

    for char in text:
        if char.isalpha():
            result.append(char.upper().translate(table))
        else:
            result.append(char)

    return ''.join(result)

# --------------------------------------------------
if __name__ == '__main__':
    main()
