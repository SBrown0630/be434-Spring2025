#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-04-23
Purpose: Create WOD
"""

import argparse
import csv
import random
from pprint import pprint
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create WOD',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='num',
                        type=int,
                        default=4)

    parser.add_argument('-f',
                        '--file',
                        help='Input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)
    wod = []
    for exercise, low, high in random.sample(exercises, k=args.num):
        reps = random.randint(low, high)
        if args.easy:
            reps = int(reps / 2)
        wod.append((exercise, reps))

    print(tabulate(wod, headers=('Exercise', 'Reps')))
# --------------------------------------------------
def read_csv(fh):
    """Read the csv input"""

    reader = csv.DictReader(fh, delimiter=',')
    exercises = [] 
    for rec in reader:
        name, reps = rec['exercise'], rec['reps']
        if name and reps:
            low, high = map(int, reps.split('-'))
            exercises.append((name, low, high))
                    
    return exercises
# --------------------------------------------------
if __name__ == '__main__':
    main()
