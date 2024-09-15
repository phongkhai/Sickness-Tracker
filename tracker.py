import gmplot
from dotenv import load_dotenv
import os

load_dotenv()

apikey = os.getenv('api_key')
gmap = gmplot.GoogleMapPlotter(37.2296,  -80.4139, 14, apikey)


#List of heatmap points and corresponding markers
attractions = [
    (37.229573, -80.423664),  # Virginia Tech Campus
    (37.224388, -80.421251),  # Hahn Horticulture Garden
    (37.220391, -80.418353),  # Lane Stadium
    (37.230298, -80.421573),  # The Moss Arts Center
    (37.298797, -80.514908),  # Pandapas Pond
    (37.229102, -80.413739),  # Downtown Blacksburg
    (37.353810, -80.599600),  # Cascades National Recreation Trail
    (37.222820, -80.427808)   # Smithfield Plantation
]

#Popularity-based weights for the attractions
weights = [5, 3, 5, 4, 4, 5, 4, 2]

#Create heatmap
gmap.heatmap(
    zip(attractions),
    radius=40,
    weights=weights,
    gradient=[(0, 0, 255, 0), (0, 255, 0, 0.9), (255, 0, 0, 1)]
)

#ADD DATA TO TEST VARIBLE!
#Add corresponding markers for each heatmap point
for idx, (lat, lng) in enumerate(attractions):
    gmap.marker(lat, lng, label=f'{idx+1}', title=f'Attraction {idx+1}')


gmap.draw('map.html')