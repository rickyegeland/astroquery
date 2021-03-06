# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
SIMBAD Query Tool
=================

The SIMBAD query tool creates a `script query
<http://simbad.u-strasbg.fr/simbad/sim-fscript>`__ that returns VOtable XML
data that is then parsed into a SimbadResult object.
This object then parses the data and returns a table parsed with `astropy.io.votable.parse`.
"""
from astropy.config import ConfigurationItem

SIMBAD_SERVER = ConfigurationItem('simbad_server', ['simbad.u-strasbg.fr',
                                                    'simbad.harvard.edu'], 'Name of the SIMBAD mirror to use.')

SIMBAD_TIMEOUT = ConfigurationItem('timeout', 60, 'time limit for connecting to Simbad server')

# O defaults to the maximum limit
ROW_LIMIT = ConfigurationItem('row_limit', 0, 'maximum number of rows that will be fetched from the result.')

from .core import Simbad, SimbadClass

__all__ = ['Simbad', 'SimbadClass']
