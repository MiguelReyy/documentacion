import csv

with open("personas.csv") as f:

    reader = csv.reader(f)
    for i in reader:
        print("Nombre1: {0}, Nombre2: {1}, Nombre3: {2}, Nombre4: {3}".format(i[0], i[1], i[2], i[3],)) 