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
                        nargs='*',
                        type=argparse.FileType('r'),
                        default=[sys.stdin])

    return parser.parse_args()
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    max_gc_id = ''
    max_gc_content = -1.0

    for fh in args.file:
        sequence_id = None
        sequence = []

        for line in fh:
            line = line.strip()
            if line.startswith('>'):
                if sequence_id is not None:
                    full_sequence = ''.join(sequence)
                    gc_content = ((full_sequence.count('G') + full_sequence.count('C')) / len(full_sequence)) * 100 if sequence else 0
                    if gc_content > max_gc_content:
                        max_gc_id = sequence_id
                        max_gc_content = gc_content
                sequence_id = line[1:]
                sequence = []
            else:
                sequence.append(line)

        if sequence_id is not None:
            full_sequence = ''.join(sequence)
            gc_content = ((full_sequence.count('G') + full_sequence.count('C')) / len(full_sequence)) * 100 if sequence else 0
            if gc_content > max_gc_content:
                max_gc_id = sequence_id
                max_gc_content = gc_content

    if max_gc_id:
        print(f'{max_gc_id} {max_gc_content:.6f}')
# --------------------------------------------------
if __name__ == '__main__':
    main()
    