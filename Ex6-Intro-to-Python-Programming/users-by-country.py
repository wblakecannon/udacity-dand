'''
Quiz: Users by Country
Let's revisit the survey information from earlier. Before we used a set to determine how many
unique countries were in the dataset. Suppose this dataset actually contains information about
users who downloaded and installed a certain application: for each user that did this their country
appears in the list. Now let's use a dict to perform a more sophisticated analysis: how many users
there are from each country?

Create a dict, country_counts whose keys are country names, and whose values are the number of
times the country occurs in the countries.py list.
'''
from countries import country_list

country_counts = {}
for country in country_list:
    country_counts[country] = country_counts.get(country, 0) + 1
    
print(country_counts)

'''
Udacity solution: 
for country in countries:
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1
'''
