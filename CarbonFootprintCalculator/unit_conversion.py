#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:51:23 2019

@author: ridwanur18
"""

# COMP 202 A1: Part 1
# Unit Conversion
# Author: Ridwanur Rahman
# ID: 260828139

import doctest
INCOMPLETE = -1

# You may find these constants important... :)
POUND_IN_KG = 0.45359237
KM_IN_MILES = 0.621371
DAYS_IN_YEAR = 365.2425


def kg_to_tonnes(kg):
    '''(num) -> float
    Convert mass in kg to in metric tonnes. 1000 kg = 1 tonne.
    >>> kg_to_tonnes(0)
    0.0
    >>> round(kg_to_tonnes(723), 4)
    0.723
    >>> round(kg_to_tonnes(0.5), 4)
    0.0005
    '''
    mass_in_tonnes = kg/1000
    return mass_in_tonnes


def pound_to_kg(lbs):
    '''(num) -> float
    Convert lbs to kg. 1 lbs is 0.453592 kg.
    >>> pound_to_kg(0)
    0.0
    >>> round(pound_to_kg(1), 4)
    0.4536
    >>> round(pound_to_kg(23), 4)
    10.4326
    '''
    mass_in_kg = lbs * 0.453592
    return mass_in_kg


def km_to_miles(km):
    '''(num) -> float
    Convert km to miles.
    >>> km_to_miles(0)
    0.0
    >>> round(km_to_miles(100), 4)
    62.1371
    >>> round(km_to_miles(5), 4)
    3.1069
    '''
    dist_in_miles = km * 0.621371
    return dist_in_miles


def daily_to_annual(daily_value):
    '''(num) -> float
    Convert a daily_value to an annual value, 
    using number of days in Gregorian year (365.2425 days).
    >>> daily_to_annual(0)
    0.0
    >>> round(daily_to_annual(1), 4)
    365.2425
    >>> round(daily_to_annual(1000), 4)
    365242.5
    '''
    annual_from_daily = daily_value * 365.2425
    return annual_from_daily


def weekly_to_annual(w):
    '''(num) -> num
    Convert a weekly amount into an annual
    amount assuming a Gregorian year of 365.2425 days.

    >>> weekly_to_annual(0)
    0.0
    >>> round(weekly_to_annual(1), 4)
    52.1775
    >>> round(weekly_to_annual(1.25), 4)
    65.2219
    '''
    annual_from_weekly = w * (365.2425/7)
    return annual_from_weekly


def annual_to_daily(annual_value):
    '''(num) -> float
    Convert a annual_value to a daily value, using number of days in Gregorian year.
    >>> annual_to_daily(0)
    0.0
    >>> annual_to_daily(365.2425)
    1.0
    >>> round(annual_to_daily(356), 4)
    0.9747
    '''
    daily_from_annual = annual_value/365.2425
    return daily_from_annual


def km_to_miles(km_value):
    '''(num) -> float
    Convert a km value to miles, 1 km = 0.621371 mile.
    >>> km_to_miles(0)
    0.0
    >>> round(km_to_miles(10), 4)
    6.2137
    >>> round(km_to_miles(50), 4)
    31.0686
    '''
    miles_value = km_value * 0.621371
    return miles_value
    

def pound_to_tonnes(lbs):
    '''(num) -> float
    Convert lbs value to tonnes.
    >>> lbs_to_tonnes(0)
    0.0
    >>> round(lbs_to_tonnes(100), 4)
    0.0454
    >>> round(lbs_to_tonnes(135), 4)
    0.0612
    '''
    to_tonnes = kg_to_tonnes(pound_to_kg(lbs))
    return to_tonnes


if __name__ == '__main__':
    doctest.testmod()
