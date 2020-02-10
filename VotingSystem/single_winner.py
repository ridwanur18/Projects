#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:29:46 2019

@author: ridwanur18
"""

# COMP 202 A3
# Name: Ridwanur Rahman
# Student ID: 260828139

from a3_helpers import *


def count_plurality(ballots):
    '''Takes as input a list of plurality ballots and returns a dictionary of how many votes each candidate got.
    (list) -> dict
    
    >>> count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL'])
    {'LIBERAL': 3, 'NDP': 1}
    '''
    
    num_of_votes = {}
    
    for candidate in ballots:
        if candidate in num_of_votes:
            num_of_votes[candidate] += 1
        else:
            num_of_votes[candidate] = 1
    
    return num_of_votes
    


def count_approval(ballots):
    '''Takes as input a list of approval ballots and returns a dictionary of how many votes each candidate got.
    (list) -> dict
    
    >>> count_approval([['LIBERAL', 'NDP'], ['NDP'], ['NDP', 'GREEN', 'BLOC']] ) 
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}
    '''
    
    flatted_ballots = flatten_lists(ballots)
    num_of_votes = count_plurality(flatted_ballots)
    
    return num_of_votes
    


def count_rated(ballots):
    '''Takes as input a list of rated ballots and returns a dictionary of how many points each candidate got.
    (list) -> dict
    
    >>> count_rated([{'LIBERAL': 5, 'NDP':2}, {'NDP':4, 'GREEN':5}])
    {'LIBERAL': 5, 'NDP': 6, 'GREEN': 5}
    '''
    
    for i in range(len(ballots)-1):
        num_of_points = add_dicts(ballots[i], ballots[i+1])
    
    return num_of_points
        

def count_first_choices(ballots):
    '''Takes as input a list of ranked ballots and returns a dictionary containing how many times each party 
    was the first choice.
    (list) -> dict
    
    >>> pr_dict(count_first_choices([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']]))
    {'BLOC': 0, 'GREEN': 1, 'LIBERAL': 0, 'NDP': 2}
    '''
    
    if len(ballots)==0:
        return {}
    
    num_of_first_choices = {}
    
    for sublist in ballots:
        for candidate in sublist:
            num_of_first_choices[candidate] = 0
        
    for sublist in ballots:
        if len(sublist) == 0:
            continue
        else:
            num_of_first_choices[sublist[0]] += 1
            
       
    return num_of_first_choices


if __name__ == '__main__':
   doctest.testmod()
    