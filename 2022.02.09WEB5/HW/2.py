from map_api.geocoder import geocode, get_ll_spn


ll, spn = get_ll_spn(input())
result = geocode(ll, {'kind': 'district'})

print(result['name'])
