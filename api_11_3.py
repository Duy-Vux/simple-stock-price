import json
import requests 

strAPI = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2020-10-27&end_date=2020-10-27&api_key=gx1daXuj2m8vbtrVKtHALsIVu8U2yvBOWcbyjch8"

response = requests.get(strAPI)

json_data = json.loads(response.text)

#Ex1:
def neo_name(json_data):
    for i in range(len(json_data["near_earth_objects"]["2020-10-27"])):
        print("Name of neo #", i, "is:", json_data["near_earth_objects"]["2020-10-27"][i]["name"])

    # for neo in json_data["near_earth_objects"]["2020-10-27"]:
    #     print(neo["name"])

neo_name(json_data)
print("\n")

#Ex2:
def diameter_min_max(json_data):
    for i in range(len(json_data["near_earth_objects"]["2020-10-27"])):
        print("Min diameter of neo #", i, "is:", json_data["near_earth_objects"]["2020-10-27"][i]["estimated_diameter"]["feet"]["estimated_diameter_min"])
        print("Max diameter of neo #", i, "is:", json_data["near_earth_objects"]["2020-10-27"][i]["estimated_diameter"]["feet"]["estimated_diameter_max"])
        print("\n")
diameter_min_max(json_data)
print("\n")

#Ex3:
def miss_distance(json_data):
    for i in range(len(json_data["near_earth_objects"]["2020-10-27"])):
        print("Miss distance of neo #", i, "is:", json_data["near_earth_objects"]["2020-10-27"][i]["close_approach_data"][0]["miss_distance"]["miles"])
        print("\n")
miss_distance(json_data)