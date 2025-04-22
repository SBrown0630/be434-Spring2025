#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-04-01
Purpose: Transcribe DNA to RNA
"""

import argparse
import os
#import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe DNA to RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILES',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input DNA file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        type=str,
                        metavar='DIR',
                        default='out')

    args = parser.parse_args()
                    
    #if os.path.isfile(args.file):
    #    args.file = open(args.file).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)


    num_seqs = 0
    num_files = 0
    for file in args.files:
        num_files += 1
        out_file = os.path.join(args.outdir,  os.path.basename(file.name))
        out_fh = open(out_file, 'wt')
        
        for dna in file:
           num_seqs += 1
           out_fh.write(dna.replace('T', 'U'))
        out_fh.close()

    print(f'Done, wrote {num_seqs} sequence{"" if num_seqs == 1 else "s"} '
          f'in {num_files} file{"" if num_files == 1 else "s"} '
          f'to directory "{args.outdir}".')
    #seq_text = "sequence"
    #file_text = "file"
    #if num_seqs > 1:
    #    seq_text = "sequences"
    #if num_files > 1:
    #    file_text = "files"

    #print(f'Done, wrote {num_seqs} {seq_text} in {num_files} {file_text} to directory "{args.outdir}".')



# --------------------------------------------------
if __name__ == '__main__':
    main()
