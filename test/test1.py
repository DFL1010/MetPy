import cartopy.crs as ccrs
import cartopy.feature as feat
import matplotlib.pyplot as plt
import numpy as np

from metpy.calc import get_wind_components
from metpy.cbook import get_test_data
from metpy.plots import StationPlot
from metpy.plots.wx_symbols import current_weather, sky_cover
from metpy.units import units

f = get_test_data('station_data.txt')

all_data = np.loadtxt(f, skiprows=1, delimiter=',', usecols=(1, 2, 3, 4, 5, 6, 7, 17, 18, 19),
                      dtype=np.dtype([('stid', '35'), ('lat', 'f'), ('lon', 'f'), ('slp', 'f'),
                                      ('air_temperature', 'f'), ('cloud_fraction', 'f'), ('dew_point_temperature', 'f'),
                                      ('weather', 'f'), ('wind_dir', 'f'), ('wind_speed', 'f')]))

# Get the full list of stations in the data
all_stids = [s.decode('ascii') for s in all_data['stid']]

# Pull out these specific stations
whitelist = []