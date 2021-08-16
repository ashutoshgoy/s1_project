countries=['India','USA','England']
friend_countries=countries[:]

countries.append('Sri_lanka')
friend_countries.append('Bangladesh')
print('original list')
for country in countries:
     print(f"countries list name {country}")
print('new_list')
for friend_country in friend_countries:
     print(f" friend_countries list name {friend_country}")
