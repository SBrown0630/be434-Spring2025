#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-05-05
Purpose: Run-length encoding/data compression
"""

import argparse
import os




# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='DNA text or file')

 
    return parser.parse_args()

# --------------------------------------------------
def encode_DNA(sequence):
    if not sequence:
        return ""

    result = []
    previous = sequence[0]
    count = 1

    for base in sequence[1:]:
        if base == previous:
            count += 1
        else:
            result.append(previous + (str(count) if count > 1 else ''))
            previous = base
            count = 1

    result.append(previous + (str(count) if count > 1 else ''))
    return ''.join(result)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if os.path.exists(args.str) and os.path.isfile(args.str):
        with open(args.str) as fh:
            for line in fh:
                print(encode_DNA(line.strip()))
    else:
        print(encode_DNA((args.str).strip()))

    
# --------------------------------------------------
if __name__ == '__main__':
    main()
