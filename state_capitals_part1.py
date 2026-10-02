import csv
import json

capitals = []

with open("state_capitals.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        capital = {
            "state": row["state"],
            "capital": row["capital"],
            "address": f"{row['state']} State Capitol, {row['capital']}, {row['state']}"
        }

        capitals.append(capital)

with open("state_capitals.json", "w") as json_file:
    json.dump(capitals, json_file, indent=4)

print("state_capitals.json created successfully.")