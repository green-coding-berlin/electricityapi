# electricityAPI

This packages gives you interfaces to various providers of electricity grid data.

Currently we only support electricitymap.org but are planing to add many more. Please leave a comment or pr if you want
to contribute more providers.

## electricitymap.org

https://www.electricitymaps.com/ is a great resource to get data about grid intensity. They also have a great api [0]
that can be used to query the data programmatically.

This package has no affiliation with https://www.electricitymaps.com/ it is just to make the querying easier. Our thanks
go out to the great people at electricitymaps for creating such an amazing project.

Currently we don't support the full api but we are working on it. Feel free to help us and submit a pull request.

We also use the free tier urls to date!!!

## Installation

```
pip install electricityapi
```

Please set the ELECTRICITYMAP_API_TOKEN if you want to use the test code provided
```
export ELECTRICITYMAP_API_TOKEN='your_api_token_here'
```

## Usage
```
import os
from electricityapi import ElectricityMap

token = os.environ.get('ELECTRICITYMAP_API_TOKEN')
em = ElectricityMap(token=token)

print(em.get_health())
print(em.get_zones())

print(em.get_carbon_intensity(zone='DE'))
print(em.get_carbon_intensity(lat=52.520008, lon=13.404954))

print(em.get_power_production(lat=52.520008, lon=13.404954))

```

[0] https://static.electricitymaps.com/api/docs/index.html#introduction