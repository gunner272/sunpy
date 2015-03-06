from __future__ import absolute_import

import numpy as np
import astropy.units as u
import warnings

from sunpy.net.attr import (Attr, AttrWalker, AttrAnd, AttrOr)
from sunpy.net.vso.attrs import Time, _VSOSimpleAttr, Wave

__all__ = ['Series', 'Protocol', 'Notify', 'Compression', 'Wave', 'Time',
           'Segment', 'walker']


class Time(Time):
    """
    Time range to download
    """


class Series(_VSOSimpleAttr):
    """
    The JSOC Series to Download.

    See `this<http://jsoc.stanford.edu/JsocSeries_DataProducts_map.html>_`
    for a list of series'.
    """
    pass


class Segment(_VSOSimpleAttr):
    """
    Segments choose which files to download when there are more than
    one present for each record e.g. 'image'
    """
    pass


class Protocol(_VSOSimpleAttr):
    """
    The type of download to request one of
    ("FITS", "JPEG", "MPG", "MP4", or "as-is").
    Only FITS is supported, the others will require extra keywords.
    """
    pass


class Notify(_VSOSimpleAttr):
    """
    An email address to get a notification to when JSOC has staged your request
    """
    pass


class Compression(_VSOSimpleAttr):
    """
    Compression format for requested files.

    'rice' or None, download FITS files with RICE compression.
    """
    pass


class Wave(Wave):
    """
    Wavelength must be specified in correct units for the series.
    """
    pass


walker = AttrWalker()


@walker.add_creator(AttrAnd, _VSOSimpleAttr, Time, Wave)
def _create(wlk, query):

    map_ = {}
    wlk.apply(query, map_)
    return [map_]


@walker.add_applier(AttrAnd)
def _apply(wlk, query, imap):

    for iattr in query.attrs:
        wlk.apply(iattr, imap)


@walker.add_applier(_VSOSimpleAttr)
def _apply(wlk, query, imap):

    imap[query.__class__.__name__.lower()] = query.value


@walker.add_applier(Time)
def _apply(wlk, query, imap):

    imap['start_time'] = query.start
    imap['end_time'] = query.end

@walker.add_applier(Wave)
def _apply(wlk, query, imap):

    if (query.min.value == query.max.value) and( query.min.unit == query.max.unit):
        imap['wavelength'] = query.min.value
    else:
        warnings.warn('Minimum and Maximum value should be same.Removing the wavelength constraint')


@walker.add_creator(AttrOr)
def _create(wlk, query):

    qblocks = []
    for iattr in query.attrs:
        qblocks.extend(wlk.create(iattr))

    return qblocks
