"""
EVE tests
"""
from __future__ import absolute_import

import pytest

#pylint: disable=C0103,R0904,W0201,W0232,E1103
import sunpy
from sunpy.lightcurve import EVELightCurve
from sunpy.data.test import (EVE_AVERAGES_CSV)
from sunpy.time import parse_time
@pytest.mark.online
def test_eve():
    eve = EVELightCurve.create('2013/04/15')
    assert isinstance(eve, EVELightCurve)


@pytest.mark.parametrize("time",
[('2013/8/7 18:00:00'),
 ('2012/4/21 02:00:00'),
 ('2012/3/11 00:01:00'),
 ('2012/5/6 23:00:00' )
])
@pytest.mark.online
def test_time(time):
    
    eve = sunpy.lightcurve.EVELightCurve.create(time)
    assert isinstance(eve,EVELightCurve)
    assert parse_time(time) in eve.data.index
    assert len(eve.data.index) == 1440


@pytest.mark.online
def test_txt():
    """Check support for parsing EVE TXT files """
    eve = EVELightCurve.create(
    "http://lasp.colorado.edu/eve/data_access/quicklook/quicklook_data/L0CS/LATEST_EVE_L0CS_DIODES_1m.txt")
    assert isinstance(eve, EVELightCurve)

def test_csv_parsing():
    """Check support for parsing EVE CSV files"""
    csv = EVELightCurve.create(EVE_AVERAGES_CSV)
    assert isinstance(csv, EVELightCurve)
