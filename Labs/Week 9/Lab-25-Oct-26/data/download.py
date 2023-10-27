#!/usr/bin/env python3
import cdsapi
c = cdsapi.Client()
c.retrieve('reanalysis-era5-complete', { # Requests follow MARS syntax
                                        # Keywords 'expver' and 'class' can be dropped. They are obsolete
                                        # since their values are imposed by 'reanalysis-era5-complete'
    'date'    : '2013-01-01/to/2013-01-31',
    'levelist': '1/10/100/137',          # 1 is top level, 137 the lowest model level in ERA5. Use '/' to separate values.
    'levtype' : 'ml',
    'param'   : '130',                   # Full information at https://apps.ecmwf.int/codes/grib/param-db/
                                        # The native representation for temperature is spherical harmonics
    'stream'  : 'oper',                  # Denotes ERA5. Ensemble members are selected by 'enda'
    'time'    : '00/to/23/by/6',         # You can drop :00:00 and use MARS short-hand notation, instead of '00/06/12/18'
    'type'    : 'an',
    'area'    : '-90/-900/90/0',          # North, West, South, East. Default: global
    'grid'    : '1.0/1.0',               # Latitude/longitude. Default: spherical harmonics or reduced Gaussian grid
    'format'  : 'netcdf',                # Output needs to be regular lat-lon, so only works in combination with 'grid'!
}, 'ERA5-ml-temperature-subarea.nc')     # Output file. Adapt as you wish.