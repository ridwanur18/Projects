#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 02:47:58 2019

@author: ridwanur18
"""

# COMP 202 A1: Part 4
# Footprint of computing and diet
# Author: Ridwanur Rahman
# ID: 260828139

import doctest
from unit_conversion import *

INCOMPLETE = -1

######################################

def fp_of_using_phone(daily_online_use, daily_phone_use):
    '''(num. num) -> float
    Estimates annual metric tonnes of CO2 from using phone.
    >>> fp_of_using_phone(0, 0)
    0.0
    >>> round(fp_of_using_phone(2, 3), 4)
    3.7902
    '''
    annual_metric_tonnes_co2 = (daily_to_annual(daily_online_use) * kg_to_tonnes(55/1000)) + (daily_phone_use * kg_to_tonnes(1250)) 
    return annual_metric_tonnes_co2
    

def fp_of_devices_bought(new_light_devices, new_medium_devices, new_heavy_devices):
    '''(num, num,num) -> float
    Estimates annual metric tonnes of CO2 from using buying new devices.
    >>> fp_of_devices_bought(0, 0, 0)
    0.0
    >>> round(fp_of_devices_bought(1, 2, 3), 4)
    2.875
    '''
    annual_metric_tonnes_co2 = (new_light_devices * kg_to_tonnes(75)) + (new_medium_devices * kg_to_tonnes(200)) + (new_heavy_devices * kg_to_tonnes(800))
    return annual_metric_tonnes_co2

    
def fp_of_computing(daily_online_use, daily_phone_use, new_light_devices, new_medium_devices, new_heavy_devices):
    '''(num, num) -> float

    Metric tonnes of CO2E from computing, based on daily hours of online & phone use, and how many small (phone/tablet/etc) & large (laptop) & workstation devices you bought.

    Source for online use: How Bad Are Bananas
        55 g CO2E / hour

    Source for phone use: How Bad Are Bananas
        1250 kg CO2E for a year of 1 hour a day

    Source for new devices: How Bad Are Bananas
        200kg: new laptop
        800kg: new workstation
        And from: https://www.cnet.com/news/apple-iphone-x-environmental-report/
        I'm estimating 75kg: new small device

    >>> fp_of_computing(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_computing(6, 0, 0, 0, 0), 4)
    0.1205
    >>> round(fp_of_computing(0, 1, 0, 0, 0), 4)
    1.25
    >>> fp_of_computing(0, 0, 1, 0, 0)
    0.075
    >>> fp_of_computing(0, 0, 0, 1, 0)
    0.2
    >>> fp_of_computing(0, 0, 0, 0, 1)
    0.8
    >>> round(fp_of_computing(4, 2, 2, 1, 1), 4)
    3.7304
    '''
    total_annual_tonnes_co2 = fp_of_devices_bought(new_light_devices, new_medium_devices, new_heavy_devices) + fp_of_using_phone(daily_online_use, daily_phone_use)
    return total_annual_tonnes_co2


######################################

def fp_of_non_vegans(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs):
    '''(num) -> float
    Estimate of annual metric tonnes of CO2 from non-vegans.
    >>> fp_of_non_vegans(0, 0, 0, 0)
    0.0
    '''
    co2_from_meat = daily_to_annual(daily_g_meat) * kg_to_tonnes(26.8/1000)
    co2_from_milk = daily_to_annual(daily_L_milk) * kg_to_tonnes(267.7777/1000)
    co2_from_cheese = daily_to_annual(daily_g_cheese) * kg_to_tonnes(12/1000)
    co2_from_eggs = daily_to_annual(daily_num_eggs) * kg_to_tonnes(300/1000)
    total_fp = co2_from_meat + co2_from_milk + co2_from_cheese + co2_from_eggs
    return total_fp

def fp_of_diet(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs):
    '''
    (num, num, num, num) -> flt
    Approximate annual CO2E footprint in metric tonnes, from diet, based on daily consumption of meat in grams, cheese in grams, milk in litres, and eggs.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    A vegan diet is 2.89 kg CO2E / day in the UK.
    I infer approximately 0.0268 kgCO2E/day per gram of meat eaten.

    This calculation misses forms of dairy that are not milk or cheese, such as ice cream, yogourt, etc.

    From How Bad Are Bananas:
        1 pint of milk (2.7 litres) -> 723 g CO2E 
                ---> 1 litre of milk: 0.2677777 kg of CO2E
        1 kg of hard cheese -> 12 kg CO2E 
                ---> 1 g cheese is 12 g CO2E -> 0.012 kg CO2E
        12 eggs -> 3.6 kg CO2E 
                ---> 0.3 kg CO2E per egg

    >>> round(fp_of_diet(0, 0, 0, 0), 4) # vegan
    1.0556
    >>> round(fp_of_diet(0, 0, 0, 1), 4) # 1 egg
    1.1651
    >>> round(fp_of_diet(0, 0, 1, 0), 4) # 1 L milk
    1.1534
    >>> round(fp_of_diet(0, 0, 1, 1), 4) # egg and milk
    1.2629
    >>> round(fp_of_diet(0, 10, 0, 0), 4) # cheeese
    1.0994
    >>> round(fp_of_diet(0, 293.52, 1, 1), 4) # egg and milk and cheese
    2.5494
    >>> round(fp_of_diet(25, 0, 0, 0), 4) # meat
    1.3003
    >>> round(fp_of_diet(25, 293.52, 1, 1), 4) 
    2.7941
    >>> round(fp_of_diet(126, 293.52, 1, 1), 4)
    3.7827
    '''
    co2_from_vegans = daily_to_annual(kg_to_tonnes(2.89))
    annual_metric_tonnes_co2 = co2_from_vegans + fp_of_non_vegans(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs)
    return annual_metric_tonnes_co2


#################################################

if __name__ == '__main__':
    doctest.testmod()

