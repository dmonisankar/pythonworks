import folium

# my_map = folium.Map(location=[22.468957, 88.317214], zoom_start =15, tiles='stamen Terrain')
my_map = folium.Map(location=[22.468957, 88.317214], zoom_start =15)
fg = folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[22.468957, 88.317214], popup="Moni Home", icon=folium.Icon(color='green')))
my_map.add_child(fg)
my_map.save('my_map1.html')
