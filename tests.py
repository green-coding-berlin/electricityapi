import os
from electricityapi import ElectricityMap

token = os.environ.get('ELECTRICITYMAP_API_TOKEN')
em = ElectricityMap(token=token)

assert(em.get_health())
assert(em.get_zones()['AD'])

assert(em.get_carbon_intensity(zone='DE')['carbonIntensity'])
assert(em.get_carbon_intensity(lat=52.520008, lon=13.404954)['carbonIntensity'])
assert(em.get_power_production(lat=52.520008, lon=13.404954)['powerConsumptionBreakdown'])

