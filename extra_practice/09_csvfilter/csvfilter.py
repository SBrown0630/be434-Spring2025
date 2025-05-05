#!/usr/bin/env python3
"""
Author : Sydalee Brown <sydaleelbrown@arizona.edu>
Date   : 2025-05-04
Purpose: Filter delimited records
"""

import argparse
import csv
import sys
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'),
                        required=True)
                    
    parser.add_argument('-v',
                        '--val',
                        metavar='val',
                        help='Value for filter',
                        type=str,
                        required=True)
                    
    parser.add_argument('-c',
                        '--col',
                        help='Column name for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    if reader.fieldnames is None:
        print(f'--file "{args.file.name}" is empty!', file=sys.stderr)
        sys.exit(1)

    if args.col and args.col not in reader.fieldnames:
        print('--col "{}" not a valid column! Choose from {}'.format(args.col, ', '.join(reader.fieldnames)), file=sys.stderr)
        sys.exit(1)

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    count = 0
                    
    for rec in reader:
        if args.col:
            val = rec.get(args.col, '')
            if re.search(args.val, val, re.IGNORECASE):
                writer.writerow(rec)
                count += 1

        else:
            for field in rec.values():
                if re.search(args.val, str(field), re.IGNORECASE):
                    writer.writerow(rec)
                    count += 1
                    break

    print(f'Done, wrote {count} to "{args.outfile.name}".')
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
