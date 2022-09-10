counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}



# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

# for county, voters in counties_dict.items():
#     print(county, voters)

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):

#       print(voting_data[i]['county'])

# for county_dict in voting_data:
#     print(county_dict['registered_voters'])



counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")