import csv
import pandas as pd

rows = []

with open("final.csv",'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        rows.append(row)

headers = rows[0]
star_data = rows[1:]

df = pd.read_csv("final.csv")
mass_list = df["Mass"].tolist()
radius_list = df["Radius"].tolist()

mass_list.pop(0)
radius_list.pop(0)

mass_siunit = []

for data in mass_list:

    si_unit = float(data)*1.989e+30
    mass_siunit.append(si_unit)

print(mass_siunit)

radius_siunit = []

for data in radius_list:
    si_unit = float(data)* 6.957e+8
    radius_siunit.append(si_unit)

print(radius_siunit)


star_masses = mass_siunit
star_radii = radius_siunit
star_names = df["Star_name"].tolist()
star_names.pop(0)

star_gravity = []

for index,data in enumerate(star_names):
    gravity = (float((star_masses[index])*5.972e+24)) / (float((star_radii[index])*(star_radii[index])*6371000*6371000) * 6.674e-11)
    star_gravity.append(gravity)

print(star_gravity)