#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-04-01
Purpose: Transcribe DNA to RNA
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe DNA to RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input DNA file')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        type=str,
                        metavar='DIR',
                        default='out')

    args = parser.parse_args()
                    
    if os.path.isfile(args.file):
        args.file = open(args.file).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.file
    outdir = open(args.outdir, 'wt') if args.outdir else sys.stdout
    rna = ''
                    
    for T in dna:
        rna = dna.replace('T', 'U')
    outdir.write(rna)
    outdir.close()



# --------------------------------------------------
if __name__ == '__main__':
    main()
