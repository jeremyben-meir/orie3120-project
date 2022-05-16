import pandas as pd
import ast

listings = pd.read_csv('listings.csv')
amenities = listings['amenities']
unique_amenity_list = []
desired_amenities = ['bathtub', 'air conditioning', 'heating', 'parking', 'tv',
        'patio', 'balcony', 'wifi', 'pool', 'dryer', 'washer', 'laundry',
        'cable', 'garage', 'gym', 'fitness center']

amenities = listings['amenities'].apply(lambda amenity_list:
        ast.literal_eval(amenity_list))
reformat_amenities = []
for amenity_list in amenities:
    reformat_amenities.append([" ".join(item.lower().strip().split()) for item in amenity_list])
listings['amenities'] = reformat_amenities
for desired_amenity in desired_amenities:
    listings[desired_amenity] = listings['amenities'].apply(lambda x: 1 if
            (desired_amenity in x) else 0)

listings['laundry'] = listings.apply(lambda row: 1 if
        row["dryer"]+row["washer"]+row["laundry"] > 0 else 0,axis=1)

listings['gym'] = listings.apply(lambda row: 1 if
        row["gym"]+row["fitness center"] > 0 else 0,axis=1)

listings['parking'] = listings.apply(lambda row: 1 if
        row["garage"]+row["parking"] > 0 else 0,axis=1)

listings.to_csv("listings.csv", index=False)
