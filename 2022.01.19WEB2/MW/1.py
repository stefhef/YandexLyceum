from map_api.geocoder import get_ll_spn, find_nearst_organization


ll, spn = get_ll_spn(input())
organization = find_nearst_organization(ll, "метро")
print(organization['properties']['name'])
