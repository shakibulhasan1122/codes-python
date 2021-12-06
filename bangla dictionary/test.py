import csv

data=csv.reader(open('Bengalidictionary_93.csv','r',encoding='utf-8'))

def search(w):
    w=w.lower()
    for row in data:
        if w==row[0]:
            return row[1]

word=input("Enter word: ")
out=search(word)
print(out)