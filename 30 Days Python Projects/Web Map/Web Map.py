import folium 

# Create a map object
# Create a feature group for the GeoJson data 

fg = folium.FeatureGroup("map") 

# Add GeoJson data to the feature group 

fg.add_child(folium.GeoJson(data=open("india_states.json", "r", 
encoding="utf-8-sig").read())) 

# Create a map object 
map = folium.Map(location=[20.0000, 75.0000], zoom_start=4) 

# Add the feature group to the map 
map.add_child(fg) 

# Display the map
# Save the map to HTML file 
map.save("final.html")