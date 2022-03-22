import folium
from folium.plugins import MarkerCluster
import pandas as pd

fmap = folium.Map(location=[24.5271, 121.4899], zoom_start=12)
tree_data = pd.read_csv('tree_atri_id.txt', encoding='big5')
sdata = tree_data.loc['櫻花','經度':'數量']
cluster_sakuras = MarkerCluster().add_to(fmap)

for lat, lng, nums in zip(sdata['緯度'], sdata['經度'], sdata['數量']) :
    num = 0
    while num < nums :
        num += 1
        folium.Marker(
            location=[lat, lng],
            icon=None,
            popup='櫻花',
            ).add_to(cluster_sakuras)
        
fmap.add_child(cluster_sakuras)
fmap.save('sak.html')
