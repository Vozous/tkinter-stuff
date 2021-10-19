import csv

def cle_pop_area_density(p):
	result = 0

	if float(p['Population']) > 0 and float(p['Area']) > 0:
		result += float(p['Population']) / float(p['Area']) 
	return result



pays = []

with open('countries.csv', mode='r', newline='') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';')
	for row in reader:
		pays.append(dict(row))


continets = list(dict.fromkeys(pay['Continent'] for pay in pays))



pays_AN = [pay for pay in pays if pay['Continent'] == continets[4]]

pays_NA = [pay for pay in pays if pay['Continent'] == continets[2]]

pays_vaste_area = [[pay for pay in pays if float(pay['Area']) > 1500000]]

world_pop = sum([ int(pay['Population']) for pay in pays ])

# print(sorted([ (p['Name'],int(p['Population'])) for p in pays if int(p['Population']) > 0], key=lambda p:p[1])[:10])


# pays.sort(key=cle_pop_area_density, reverse=True)

# print([ p['Name'] for p in pays][:8])