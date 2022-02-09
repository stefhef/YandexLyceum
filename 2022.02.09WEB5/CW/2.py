import sys
from map_api.geocoder import get_ll_spn, show_map, get_nearst_object

toponym_to_find = ' '.join(sys.argv[1:])

ll, spn = get_ll_spn(toponym_to_find)
show_map(ll, spn, add_params={"pt": f"{ll},pm2rdm"})
