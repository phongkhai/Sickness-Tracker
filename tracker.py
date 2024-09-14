import gmplot

#Google Maps API
#Create the map plotter:

gmap = gmplot.GoogleMapPlotter(37.229572, -80.413940, 14, apikey=apikey)


#List of heatmap points and corresponding markers
attractions = [
    (37.769901, -122.498331),
    (37.768645, -122.475328),
    (37.771478, -122.468677),
    (37.769867, -122.466102),
    (37.767187, -122.467496),
    (37.770104, -122.470436)
]

#List of heatmap points and corresponding markers
attractions = [
    (37.769901, -122.498331),
    (37.768645, -122.475328),
    (37.771478, -122.468677),
    (37.769867, -122.466102),
    (37.767187, -122.467496),
    (37.770104, -122.470436)
]

#Add corresponding markers for each heatmap point
for idx, (lat, lng) in enumerate(attractions):
    gmap.marker(lat, lng, label=f'{idx+1}', title=f'Attraction {idx+1}')

#Draw the map:

gmap.draw('map.html')