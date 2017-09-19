import csv
import pprint

fieldname = "wgs84_pos#lat"
minval = -90
maxval = 90



client = MongoClient("mongodb://localhost:27017")


def skip_lines(input_file, skip):
    for i in range(0, skip):
        next(input_file)

def audit_country(input_file):
    for row in input_file:
        country = row['country_label']
        country = country.strip()
        if (country == 'NULL') or (country == ""):
            continue
        if db.countries.find({"name" : country }).count() != 1:
            print "Not found:", country

if __name__ == '__main':
    input_file = csv.DictReader(open("cities.csv"))
    skip_lines(input_file, )