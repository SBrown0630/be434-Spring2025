#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-04-22
Purpose: Sing bottles of beer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Sing bottles of beer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-n',
                        '--num',
                        help='Number of verses',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
                    
    verses = [verse(n) for n in range(args.num, 0, -1)]
        #verses.append(verse(n))

    print('\n\n'.join(verses))

# --------------------------------------------------
def verse(bottle):
    """ Sing a verse """

    next_bottle = bottle - 1
    s1 = '' if bottle == 1 else 's'
    s2 = '' if next_bottle == 1 else 's'
    next_num = 'No more' if next_bottle == 0 else next_bottle

    return '\n'.join([
        f'{bottle} bottle{s1} of beer on the wall,', 
        f'{bottle} bottle{s1} of beer,', 
        'Take one down, pass it around,',
        f'{next_num} bottle{s2} of beer on the wall!'
    ])

# --------------------------------------------------
if __name__ == '__main__':
    main()
