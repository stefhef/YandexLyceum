from map_api.geocoder import get_ll_spn, show_map
from map_api.distance import lonlat_distance

ostan_cords = (37.611704, 55.819721)
ll, spn = get_ll_spn('Пермь')
dist = lonlat_distance(ostan_cords, tuple(map(float, ll.split(','))))
h2 = (dist / 3.6 - 525 ** 0.5) ** 2
print(h2)
show_map(ll, spn)
