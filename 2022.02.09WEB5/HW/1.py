from map_api.geocoder import get_ll_spn, find_organization, show_map


ll, spn = get_ll_spn('Ветлужская 89')
organizations = find_organization(ll, 'аптека')
params = {"pt": []}
for number, d in enumerate(organizations):
    if number == 11:
        break
    cords = ",".join(map(str, d["geometry"]["coordinates"]))
    tp = d['properties']['CompanyMetaData']['Hours']['text']
    if 'круглосуточно' in tp:
        params['pt'].append(f'{cords},pm2gnm')
    elif '-' in tp:
        params['pt'].append(f'{cords},pm2blm')
    else:
        params['pt'].append(f'{cords},pm2grm')

params['pt'] = '~'.join(params['pt'])
show_map(ll, '0.02,0.02', add_params=params)
