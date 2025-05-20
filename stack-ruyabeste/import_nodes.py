import csv

class Node:
    def __init__(self, id, lat, lon, name):
        self.id = id
        self.lat = float(lat)
        self.lon = float(lon)
        self.name = name
        

def import_csv(file):
    nodes = []
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')  
        for row in reader:
            nodes.append(Node(row['id'], row['latitude'], row['longitude'], row['name']))
    return nodes