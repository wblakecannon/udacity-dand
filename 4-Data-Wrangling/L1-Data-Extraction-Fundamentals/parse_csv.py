import os
import pprint
import csv

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile, 'rb') as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
    return data

if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    parse_csv(datafile)
    d = parse_csv(datafile)
    pprint.pprint(d)
