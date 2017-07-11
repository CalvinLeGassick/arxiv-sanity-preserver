import csv
import pickle
import sys

if __name__ == "__main__":
    keywords = sys.argv[1:]
    db = pickle.load(open("db.p", "rb"))
    to_write = []
    papers = []
    for ID, paper in sorted(db.items()):
        abstract = paper["summary"].replace("\n", " ")
        skip = False
        for k in keywords:
            if k not in abstract:
                skip = True
        if skip:
            continue

        title = paper["title"]
        time = paper["published"]
        link = paper["link"]
        papers.append([ID, time, title, abstract, link])

    with open('%s.csv' % "_".join(keywords), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["ID", "Published", "Title", "Abstract", "Link"])
        for p in papers:
            writer.writerow(p)
