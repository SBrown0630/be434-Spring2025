#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-03-16
Purpose: Compute GC content
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input sequence file',
                        nargs=1,
                        type=argparse.FileType('r'),
                        default=[sys.stdin])

    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
args = get_args()

sequence_id = ''
sequence = ''
max_gc_content = -1
max_gc_id = ''

for line in args.file:
    line = line.rstrip()
    if line.startswith('>'):
        gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_id = sequence_id
        sequence_id = line[1:]  
        sequence = ''
    else:
        sequence += line  
gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence)
if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_id = sequence_id
# Print the result
print(f'{max_gc_id} {max_gc_content:.6f}')
# --------------------------------------------------
if __name__ == '__main__':
    main()