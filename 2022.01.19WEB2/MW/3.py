from map_api.distance import lonlat_distance
from map_api.geocoder import get_ll_spn

ll1, spn1 = get_ll_spn(input())
ll2, spn2 = get_ll_spn(input())
dist = lonlat_distance(map(float, ll1.split(',')), map(float, ll2.split(',')))
print(f'От дома до школы: {round(dist, 2)} м')
