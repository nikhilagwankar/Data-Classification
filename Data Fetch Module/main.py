import sys
import urlFetchData
import os
import pandas as pd
import csv

def main(argv):
    urls = []
    with open("data.csv","r",encoding='utf-8') as f:
        reader = csv.DictReader(f)
        #print(reader);
        for row in reader:
            #print(row['url'])
            urls.append(row['url'])

    #lets open our file
    fo = open(argv[1],"w",encoding='utf-8')
    fo.write("{ \"data\": [")
    #call the function to fetch data from url
    for url in urls:
        fo.write("{")
        fo.write(urlFetchData.urlFetchData(url))
        fo.write("},")
    fo.seek(-1, fo)
    fo.truncate()
    fo.write("]}")
    fo.close()

if __name__ == "__main__":
  main(sys.argv)