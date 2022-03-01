import json
from zipfile import ZipFile

count = 0
with ZipFile("input.zip") as myzip:

    for elem in myzip.infolist():
        filename = elem.filename
        filename: str
        if filename[-1] != '/' and filename.endswith(".json"):
            with myzip.open(filename) as file:
                data = json.load(file)
                if data["city"] == "Москва":
                    count += 1

print(count)
