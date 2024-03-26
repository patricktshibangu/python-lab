import csv

with open("work23.csv", 'w') as f:
    pen = csv.writer(f)
    header = ["name" , "cell Phone" , "city"]
    pen.writerow(header)
    pen.writerow(["patrick" , "999 999 999" , "lexington"])
f.close
