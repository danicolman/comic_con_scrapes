# grab AA info from ECCC website and dump into spreadsheet
import requests
import json
import pprint
import csv

url = "https://api-melupufoagt.stackpathdns.com/api/space_orders"

headers = {"Accept": "application/json"}

query = {
    "specials": 1,
    "key": "c2bc1038-e140-493e-8316-93d221b76847",
    "category": "13504"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
)

artist_alley = []

AA_all_info = response.json()["space_orders"]

for artist in AA_all_info:
    vendor = {}
    vendor.update({
        "Company": artist["company"],
        "First Name": artist["first_name"],
        "Last Name": artist["last_name"],
        "Table": artist["booth"],
        "Website": artist["website"]
    })
    artist_alley.append(vendor)

with open("ECCC_AA.csv", "w") as eccc_aa_csv:
    artist_writer = csv.writer(eccc_aa_csv)

    count = 0

    for artist in artist_alley:
        if count == 0:
            header = artist.keys()
            artist_writer.writerow(header)
            count += 1

        artist_writer.writerow(artist.values())
