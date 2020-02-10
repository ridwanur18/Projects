#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:21:08 2019

@author: ridwanur18
"""

# COMP 202 A3
# Name: Ridwanur Rahman
# ID: 260828139

from single_winner import *
import math

################################################################################

def votes_needed_to_win(ballots, num_winners):
    '''Takes as input a list of ballots and an integer number of winners and returns the integer 
    number of votes a candidate would need to win the Droop Quota.
    (list, num) -> num
    
    >>> votes_needed_to_win([{'CPC':3, 'NDP':5}, {'NDP':2, 'CPC':4}, {'CPC':3, 'NDP':5}], 1)
    2
    >>> votes_needed_to_win(['g']*20, 2)
    7
    >>> votes_needed_to_win([['NDP'], ['GREEN', 'NDP', 'BLOC'], ['LIBERAL','NDP'], ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'], ['BLOC', 'CPC'], ['LIBERAL', 'GREEN'], ['NDP']], 1)
    5
    '''
    
    total_votes = len(ballots)
    
    return (math.floor(total_votes/(num_winners+1)) + 1)
    
    

def has_votes_needed(result, votes_needed):
    '''Takes as input a dictionary of election results and integer votes needed and returns a boolean
    representing whether the candidate with the most votes in this election has at least votes_needed
    votes.
    (dict, num) -> bool
    
    >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3}, 4)
    True
    '''
    
    if result == {}:
        return False
        
    winner = get_winner(result)
    if result[winner] >= votes_needed:
        return True
    
    return False
    

################################################################################


def eliminate_candidate(ballots, to_eliminate):
    '''Takes as input a list of ranked ballots and a list of candidates to eliminate. Returns a new list 
    of ranked ballots where all the candidates in to_eliminate have been removed.
    (list, list) -> list
    
    >>> eliminate_candidate([['LIBERAL', 'NDP'], ['GREEN', 'NDP'], ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
    [[], ['GREEN'], ['BLOC']]
    >>> eliminate_candidate([['CPC', 'NDP'], ['GREEN', 'LIBERAL'], ['LIBERAL']], ['LIBERAL'])
    [['CPC', 'NDP'], ['GREEN'], []]'''
    
    ballots_copy = [[] for i in range(len(ballots))]
    
    for i in range(len(ballots)):
        for candidate in ballots[i]:
            if candidate in to_eliminate:
                continue
            else:
                ballots_copy[i].append(candidate)
            
    return ballots_copy
    


################################################################################


def count_irv(ballots):
    '''Takes as input a list of ranked ballots and returns a dictionary of how many votes each candidate
    ends with after counting with IRV.
    (list) -> dict
    
    >>> pr_dict(count_irv([['NDP'], ['GREEN', 'NDP', 'BLOC'], ['LIBERAL','NDP'], ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'], ['BLOC', 'CPC'], ['LIBERAL', 'GREEN'], ['NDP']]))
    {'BLOC': 0, 'CPC': 0, 'GREEN': 0, 'LIBERAL': 3, 'NDP': 5}
    '''
    
    candidate_initial = {}
    candidate_list = get_all_candidates(ballots)
    for candidates in candidate_list:
        candidate_initial[candidates] = 0
    
    first_choices = count_first_choices(ballots)
    votes_needed = votes_needed_to_win(ballots, 1)
    
    while not has_votes_needed(first_choices, votes_needed):
       to_eliminate = [last_place(first_choices)]
       ballots = eliminate_candidate(ballots, to_eliminate)
       first_choices = count_first_choices(ballots)
       if flatten_dict(first_choices) == []:
           break
                    
    result = add_dicts(first_choices, candidate_initial)
    
    return result
    

################################################################################

if __name__ == '__main__':
    doctest.testmod()
#    g = ['GREEN', 'NDP', 'BLOC']
#    n = ['NDP', 'GREEN', 'BLOC']
#    eliminate_candidate([g]*5 + [n]*3, 'GREEN')