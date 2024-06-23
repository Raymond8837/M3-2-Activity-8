import csv
with open('contacts.csv', newline='') as csvfile:
    contacts = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in contacts:
        print(', '.join(row))
