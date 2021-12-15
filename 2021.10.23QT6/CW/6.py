import sys
import csv

headers = ('nomen', 'definitio', 'pluma', 'Russian nomen', 'familia', 'Russian nomen familia')
data = list(map(lambda x: x.rstrip().split('\t'), sys.stdin))
with open('plantis.csv', 'w', encoding='utf8') as out_file:
    writer = csv.writer(out_file, delimiter=';')
    writer.writerow(headers)
    writer.writerows(data)
