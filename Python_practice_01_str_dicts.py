print("Hello world")

help("keywords")

print((8 // 5) - 3)


counties = ["Arapahoe","Denver","Jefferson"]

counties[0:2]


counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))

print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))


voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})

#print(voting_data)
voting_data.pop(0)
voting_data.pop(1)
voting_data.insert(2, {"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

print(voting_data)