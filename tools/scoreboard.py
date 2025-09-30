#!/usr/bin/env python3
# Very small scoreboard generator: reads a CSV `results.csv` and prints simple table.
import csv, sys
def show(path='tools/results.csv'):
    try:
        with open(path) as f:
            rows = list(csv.reader(f))
    except FileNotFoundError:
        print('No results.csv found at', path)
        return
    print('\t'.join(rows[0]))
    for r in rows[1:]:
        print('\t'.join(r))
if __name__ == '__main__':
    p = sys.argv[1] if len(sys.argv)>1 else 'tools/results.csv'
    show(p)
