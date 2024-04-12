import csv

personas = [
    ["Palacios","Lopez","Anda"," Rey", ]
]

with open("escrito.csv", "w", newline="")as file:

    writer = csv.writer(file, delimiter=",")
    writer.writerow(personas) # si ponemos writerows se respetan las lineas del texto 