
# Uicar algorith to detect same directions with all the data from firebase 

# The program should = get the data from fireabase the directions, put into a matriz and compare 


# Get the location in a zone night hour like 4am, then taking in the daytime hour like 12 am, , if the patron is the same few, match them 

import pandas as pd 
import json
import matplotlib.pyplot as plt


from math import sin, cos, sqrt, atan2, radians



with open('models/data-1.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)


with open('models/data-2.json', 'r') as f:
    data = json.load(f)
df2 = pd.DataFrame(data)


# print(df.head())


data1 = df.drop(["County", "District", "Local Authority" , "Area(m2)" , "CAV Details"], axis=1)

data2 = df2.drop(["County", "District", "Local Authority" , "Area(m2)" , "CAV Details"], axis=1)





def comparedistante( lat1, lon1, lat2, lon2):

    match = False

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c


    print("Result:", distance)
    print("Should be:", distance, "km")

    if distance == 0:
        print('Same fucking place')
        # family or friends
    
    elif distance <= 1:
        print('Good distance')
        match = True
    else: 
        print('To far')
        match = False





# print(data.head())


# for index, row in data.iterrows():
#     comparedistante( row['X'] , row['Y'])


# approximate radius of earth in km
data1.plot(kind='scatter',x='X',y='Y',color='red')
data2.plot(kind='scatter',x='X',y='Y',color='blue')
plt.show()


R = 6373.0


array = [ 52.2296756 , 21.0122287]

array2 = [ 52.2276756, 21.0122287  ]

lat1 = radians(52.2296756)
lon1 = radians(21.0122287)
lat2 = radians(52.2276756)
lon2 = radians(21.0122287)





        

comparedistante(lat1, lon1, lat2, lon2)


data.median(axis=0)
print(data.median(axis=0), "Hola")