#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:40:35 2019

@author: ridwanur18
"""

# COMP 202 A3 Part 1
# Name: Ridwanur Rahman
# Student ID: 260828139

import doctest
import random

def flatten_lists(nested):
    '''Takes as input a list that contains list(s) and returns a new version of the list which is flattened.
    (list) -> list
    
    >>> flatten_lists([[0], [1, 2], 3])
    [0, 1, 2, 3]
    >>> flatten_lists([[9, 8, 6], [4, 4], 1, 2])
    [9, 8, 6, 4, 4, 1, 2]
    >>> flatten_lists([['Water', 'Beer', 'Wine'], 'Chocolate', 'Rock', 'Stone'])
    ['Water', 'Beer', 'Wine', 'Chocolate', 'Rock', 'Stone']
    '''
    
    flat_list = []
    for sublist in nested:
        if type(sublist) == int or type(sublist) == str:
            flat_list.append(sublist)
        else:
            for x in sublist:
                flat_list.append(x)
            
    return flat_list


def flatten_dict(d):
    '''Takes as input a dictionary of non-negative keys and returns a list of the keys of the dictionary with
    each v repeated v times, where v is the value associated with each of the keys.
    (dict) -> list
    
    >>> flatten_dict({'LIBERAL': 5, 'NDP':2})
    ['LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'NDP', 'NDP']
    >>> flatten_dict({'OXYGEN': 0, 'ARGON': 1})
    ['ARGON']
    '''
    
    d_list = []
    for key in d:
        for v in range(d[key]):
            d_list.append(key)
    
    return d_list


def add_dicts(d1, d2):
    '''Takes two dictionaries where all keys are numbers as input and merges them, adding keys if they are in both 
    dictionaries and returns the resulting dictionary.
    (dict, dict) -> dict
    
    >>> add_dicts({'a':5, 'b':2, 'd':-1}, {'a':7, 'b':1, 'c':5})
    {'a': 12, 'b': 3, 'd': -1, 'c': 5}
    '''
    
    new_dict = {}
    for key in d1:
        new_dict[key] = d1[key]
    
    for key in d2:
        if key in new_dict:
            new_dict[key] += d2[key]
        else:
            new_dict[key] = d2[key]
    
    return new_dict


def get_all_candidates(ballots):
    '''takes as input a list which can contain strings, lists, dictionaries or a mix of the three
    and returns all the unique strings in the list and its nested contents.
    (list) -> list
    
    >>> get_all_candidates([{'GREEN':3, 'NDP':5}, {'NDP':2, 'LIBERAL':4}, ['CPC', 'NDP'], 'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']
    '''
    
    candidates_list = []
    for sub in ballots:
        if type(sub) == str:
            candidates_list.append(sub)
        elif type(sub) == list:
            for s in sub:
                if s in candidates_list:
                    continue
                else:
                    if type(s) == str:
                        candidates_list.append(s)
        else:
            if type(sub) == dict:
                for key in sub:
                    if key in candidates_list:
                        continue
                    else:
                        candidates_list.append(key)
                    
    return candidates_list


###################################################### winner/loser

def get_candidate_by_place(result, func):
    '''Takes as input a dictionary and a function and returns the key of the dictionary corrresponding
    to the function value.
    (dict) -> str
    
    >>> result = {'LIBERAL' : 5, 'NDP' : 6, 'CPC' : 6, 'GREEN' : 4}
    >>> get_candidate_by_place(result, min)
    'GREEN'
    >>> random.seed(0)
    >>> get_candidate_by_place(result, max)
    'CPC'
    >>> random.seed(1)
    >>> get_candidate_by_place(result, max)
    'NDP'
    '''
    
    if func == max:
        return get_winner(result)
    else:
        return last_place(result, seed = None)        
        
            
def get_winner(result):
    '''Takes as input a dictionary with the same format as above and returns the key with the greatest value, 
    breaking ties randomly if there are any.
    (dict) -> str
    
    >>> get_winner({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0})
    'NDP'
    >>> random.seed(0)
    >>> get_winner({'NDP': 7, 'GREEN': 2, 'LIBERAL': 7, 'BLOC': 3, 'CPC': 7})
    'LIBERAL'
    >>> random.seed(1)
    >>> get_winner({'NDP': 7, 'GREEN': 2, 'LIBERAL': 7, 'BLOC': 3, 'CPC': 7})
    'NDP'
    >>> random.seed(2)
    >>> get_winner({'NDP': 7, 'GREEN': 2, 'LIBERAL': 7, 'BLOC': 3, 'CPC': 7})
    'NDP'
    '''
    
    if result == {}:
        return ''
    
    keys = []
    max_value = max(result.values())
    for key, value in result.items():
        if value == max_value:
            keys.append(key)
    
    return random.choice(keys)


def last_place(result, seed = None):
    '''Takes as input a dictionary with the same format as above and returns the key with the lowest value,
    breaking ties randomly if there are any.
    
    >>> last_place({'NDP': 2, 'GREEN': 1, 'LIBERAL': 5, 'BLOC': 0})
    'BLOC'
    >>> random.seed(0)
    >>> last_place({'NDP': 4, 'GREEN': 4, 'LIBERAL': 7, 'BLOC': 4, 'CPC': 5})
    'GREEN'
    >>> random.seed(1)
    >>> last_place({'NDP': 4, 'GREEN': 4, 'LIBERAL': 7, 'BLOC': 4, 'CPC': 5})
    'NDP'
    >>> random.seed(2)
    >>> last_place({'NDP': 4, 'GREEN': 4, 'LIBERAL': 7, 'BLOC': 4, 'CPC': 5})
    'NDP'
    '''
    
    if result == {}:
        return ''
    
    keys = []
    min_value = min(result.values())
    for key, value in result.items():
        if value == min_value:
            keys.append(key)

    return random.choice(keys)


###################################################### testing help

def pr_dict(d):
    '''(dict) -> None
    Print d in a consistent fashion (sorted by key).
    Provided to students. Do not edit.
    >>> pr_dict({'a':1, 'b':2, 'c':3})
    {'a': 1, 'b': 2, 'c': 3}
    '''
    l = []
    for k in sorted(d):
        l.append( "'" + k + "'" + ": " + str(d[k]) )
    print('{' + ", ".join(l) + '}')


if __name__ == '__main__':
    doctest.testmod()
    