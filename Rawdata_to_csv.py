import csv
import os

title = "label content".split(" ")

print(type(title))

f = open('voice.csv',"w",encoding="utf-8")
w = csv.writer(f)

w.writerow(title)

root = "/Users/minyoung/Desktop/temp_data/"
list = os.listdir(root)

for cat in list:
    if cat not in '.DS_Store':
        print(cat)
        files = os.listdir(root + cat)

        for file in files:
            if file not in '.DS_Store':
                #print(file)
                address = root + cat + "/" + file

                content = open(address, "r", encoding = "utf-8")
                strings = content.read()

                w.writerow([cat,strings])

f.close()