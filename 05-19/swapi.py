import requests

response = requests.get("https://swapi.dev/api/people/1")

luke = response.json()

print(luke["name"])
print(luke["height"])
print(luke["starships"])
print(luke["starships"][0])

response2 = requests.get("https://swapi.dev/api/starships/12")

s12 = response2.json()

print(s12["name"])
print(s12["model"])
print(s12["films"])
print(s12["films"][1])

people_response = requests.get("https://swapi.dev/api/people/")

people = people_response.json()

print("Všechna jména postav, co najdete v SW apíčku, jsou zde:")
for person in people["results"]:
    print(person["name"])

print("První člověk je:")
print(people["results"][0]["name"])

print("Dalších pět lidí je:")
print(people["results"][1]["name"])
print(people["results"][2]["name"])
print(people["results"][3]["name"])
print(people["results"][4]["name"])
print(people["results"][6]["name"])


