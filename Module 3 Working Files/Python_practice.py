#Create list of dictionaries for counties and number of registered voters
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
#Iterate over list to store individual dictionaries using county_dict variable
for county_dict in voting_data:
    #Store values for "county" keys using county variable
    county = county_dict["county"]
    #Store values for "registered_voters" keys using voters variable
    voters = county_dict["registered_voters"]
    #Display outputs in legible sentences for users
    print(f'{county} county has {voters:,} registered voters.')
        