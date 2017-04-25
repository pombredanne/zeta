# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.


"""
How DateTime is managed in Zeta ?
  * All date-time values are stored in database as UTC time zone.
  * When ever user provides a date-time value, it will be converted to
    UTC before storing them into the database.
  * Before rendering the date-time value from the data base to the client
    terminal, they will be converted to User's local time zone.
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
#   * Looks like the timezone information has changed across the decades /
#     centuries and so, the time-delta between different timezone seem to be
#     varying. The following mail thread could explain a bit.
#       
#       URL : http://mail.python.org/pipermail/python-list/2007-July/448982.html
#
#     On Jul 12, 11:47 am, Sanjay <skpate... at gmail.com> wrote:
#       > Hi All,
#       >
#       > Using pytz, I am facing a problem with Asia/Calcutta, described below.
#       >
#       > Asia/Calcutta is actually IST, which is GMT + 5:30. But while using
#       > pytz, it was recognized as HMT (GMT + 5:53). While I digged into the
#       > oslan database, I see the following:
#       >
#       > # Zone NAME GMTOFF RULES FORMAT [UNTIL]
#       > Zone Asia/Calcutta 5:53:28 - LMT 1880 # Kolkata
#       >                5:53:20 - HMT 1941 Oct # Howrah Mean Time?
#       >                6:30 - BURT 1942 May 15 # Burma Time
#       >                5:30 - IST 1942 Sep
#       >                5:30 1:00 IST 1945 Oct 15
#       >                5:30 - IST
#       >
#       > Searching in this group, I saw a similar problem posted
#       > at
#       > http://groups.google.co.in/group/comp.lang.python/browse_thread/threa...
#       > without any solutions.
#       >
#       > I mailed to Stuart and also posted it at the launchpad of pytz, but
#       > did not get any response.
#       >
#       > Unable to know how to proceed further. Any suggestion will be of vital
#       > help.
#       >
#       > thanks
#       > Sanjay
#
#       I don't use pytz myself that often so I can't be sure, but I don't
#       think it's a bug in pytz.
#
#       The problem seems to be that the timezone has changed for the
#       location. Now, without a date as reference, pytz can't know what
#       timezone to use when constructing the tzinfo; you might want a date
#       from the 1800's.
#
#       When you're constructing the datetime with the tzinfo argument, you're
#       saying: use this timezone as the local timezone. datetime_new (the
#       constructor in C) never calls the tzinfo to verify that the timezone
#       is still valid, it just uses it.
#
#       On the other hand: When you construct a datetime with datetime.now()
#       and pass a timezone, datetime_now (again, in C) calls the method
#       fromutz() on the tzinfo object. Now the pytz tzinfo object has a
#       reference by which to choose the current timezone for the location,
#       and that's why it's correct when you use datetime.now() but not for a
#       manual construction.
#
#       A "workaround" (or maybe the proper way to do it) is to construct the
#       datetime without a tzinfo set, and then use the localize() method on
#       the tzinfo object, this will give you the correct result.
#
#       >>> tz = pytz.timezone("Asia/Calcutta")
#       >>> mydate = datetime.datetime(2007, 2, 18, 15, 35)
#       >>> print tz.localize(mydate)
#       2007-02-18 15:35:00+05:30
# Todo    : 
#   1. usertz_2_utc() function currently accepts only `datetime` object. Fix
#      it so that it can accept wide variery of date-time format.

import logging
from   datetime import datetime, timedelta
from   pytz     import timezone, all_timezones, utc
import pytz     

log = logging.getLogger( __name__ )

is_tz  = lambda tzname : tzname in pytz.all_timezones
utcnow = lambda : datetime.utcnow()

def usertz_2_utc( userdt, usertz=None ):
    """User provided date-time value should be converted to UTC timezone.

    `userdt`  can be an `aware` instance of datetime.datetime. Otherwise
              `usertz` should be provided."""
    usertz = isinstance( usertz, (str, unicode)) and timezone(usertz) or usertz
    userdt = userdt.tzinfo and userdt or usertz.localize( userdt )
    utcdt  = userdt.astimezone( timezone( 'UTC' ))
    return utcdt

def utc_2_usertz( utcdt, usertz ) :
    """DateTime from database is in UTC timezone. Convert that into user
    timzone specifed by `usertz`.

    `utcdt`     can be an `aware` instance of datetime.datetime. Otherwise it
                will be localized to 'UTC' timezone.
    `usertz`    string or `tzinfo`.
    """
    usertz = isinstance( usertz, (str, unicode)) and timezone(usertz) or usertz
    utcdt  = utcdt.tzinfo and utcdt or timezone('UTC').localize( utcdt )
    userdt = utcdt.astimezone( usertz )
    return userdt

def timeinfuture( somedt ) :
    """Check whether the passed DateTime instance is representing time in
    future or past.

    Return True, if the time is in future. Else False.
    """
    userdt   = somedt.tzname() != 'UTC' and usertz_2_UTC( somedt ) or somedt
    timelist = list(datetime.timetuple(datetime.utcnow()))[:7] + \
               [ timezone('UTC') ]
    curr_udt = datetime( *timelist )
    diff     = userdt - curr_udt
    if diff.days < 0 or diff.seconds < 0 or diff.microseconds < 0 :
        return False
    else :
        return True
