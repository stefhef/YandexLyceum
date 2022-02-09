import sys
from map_api.geocoder import get_ll_spn, show_map, get_nearst_object

toponym_to_find = "Ветлужская 89"

ll, spn = get_ll_spn(toponym_to_find)
responce = get_nearst_object(ll, spn)
show_map(responce)
