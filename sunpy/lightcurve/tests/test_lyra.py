"""
Lyra Tests
"""
from __future__ import absolute_import

import pytest

#pylint: disable=C0103,R0904,W0201,W0232,E1103
import sunpy
import matplotlib as mpl
from matplotlib.testing.decorators import cleanup
from sunpy.lightcurve import LYRALightCurve
from sunpy.time import TimeRange
@pytest.mark.online
def test_lyra():
    lyra = sunpy.lightcurve.LYRALightCurve.create(
    "http://proba2.oma.be/lyra/data/bsd/2011/08/10/lyra_20110810-000000_lev2_std.fits")
    assert isinstance(lyra, sunpy.lightcurve.LYRALightCurve)


@pytest.mark.parametrize("time",
[('2013/8/7 18:00:00'),
 ('2012/4/21 02:00:00'),
 ('2011/3/11 00:00:00'),
 ('2012/5/6 23:59:59' )
])
@pytest.mark.online
def test_time(time):
    
    lyra= LYRALightCurve.create(time)
    assert isinstance(lyra,LYRALightCurve)
    assert len(lyra.data.index) == 1440


@pytest.mark.parametrize("start, end",
[(('2013/8/7 18:00:00') ,('2013/8/7 19:00:00')),
 (('2011/3/11 00:00:00'),('2011/3/11 00:10:00')),
 (('2012/5/6 23:19:59' ),('2012/5/6 23:59:59' ))
])
@pytest.mark.online
def test_date(start,end):

    lyra = LYRALightCurve.create(start,end)
    assert isinstance(lyra,LYRALightCurve)


@pytest.mark.parametrize("timerange",
[(TimeRange(('2013/8/7 18:00:00') ,('2013/8/7 19:00:00'))),
 (TimeRange(('2012/4/21 02:00:00'),('2012/4/22 02:00:00'))),
 (TimeRange(('2011/3/11 00:00:00'),('2011/3/13 00:00:00'))),
])
@pytest.mark.online
def test_timerange(timerange):
    
    lyra = LYRALightCurve.create(timerange)
    assert isinstance(lyra, LYRALightCurve)


#@cleanup
#def test_peek():
#    lyra = sunpy.lightcurve.LYRALightCurve.create(
#    "http://proba2.oma.be/lyra/data/bsd/2011/08/10/lyra_20110810-000000_lev2_std.fits")
#    assert isinstance(lyra.peek(),mpl.figure.Figure)
