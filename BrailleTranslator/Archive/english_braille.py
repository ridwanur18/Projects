#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:50:32 2019

@author: ridwanur18
"""

# COMP 202 A2 Part 5
# Author: Ridwanur Rahman

from text_to_braille import *
from to_unicode import *
from helpers import *
from char_to_braille import *

ENG_CAPITAL = '..\n..\n.o'
ENG_NUMBER_START = '.o\n.o\noo'
ENG_NUMBER_END = '..\n.o\n.o'
PUNCTUATION_ENG_1 = ',;:.'
PUNCTUATION_ENG_2 = '\“*\”'

####################################################
# Here are two helper functions to help you get started

def two_letter_contractions(text):
    '''(str) -> str
    Process English text so that the two-letter contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.
    Provided to students. You should not edit it.

    >>> two_letter_contractions('chat')
    'âat'
    >>> two_letter_contractions('shed')
    'îë'
    >>> two_letter_contractions('shied')
    'îië'
    >>> two_letter_contractions('showed the neighbourhood where')
    'îœë ôe neiêbürhood ûïe'
    >>> two_letter_contractions('SHED')
    'ÎË'
    >>> two_letter_contractions('ShOwEd tHE NEIGHBOURHOOD Where') 
    'ÎŒË tHE NEIÊBÜRHOOD Ûïe'
    '''
    combos = ['ch', 'gh', 'sh', 'th', 'wh', 'ed', 'er', 'ou', 'ow']
    for i, c in enumerate(combos):
        text = text.replace(c, LETTERS[-1][i])
    for i, c in enumerate(combos):
        text = text.replace(c.upper(), LETTERS[-1][i].upper())
    for i, c in enumerate(combos):
        text = text.replace(c.capitalize(), LETTERS[-1][i].upper())

    return text


def whole_word_contractions(text):
    '''(str) -> str
    Process English text so that the full-word contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    If the full-word contraction appears within a word, 
    contract it. (e.g. 'and' in 'sand')

    Provided to students. You should not edit this function.

    >>> whole_word_contractions('with')
    'ù'
    >>> whole_word_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meow'
    >>> whole_word_contractions('With')
    'Ù'
    >>> whole_word_contractions('WITH')
    'Ù'
    >>> whole_word_contractions('wiTH')
    'wiTH'
    >>> whole_word_contractions('FOR thE Cat WITh THE purr And The meow')
    'É thE Cat WITh À purr Ç À meow'
    >>> whole_word_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> whole_word_contractions('wither')
    'ùer'
    '''
    # putting 'with' first so wither becomes with-er not wi-the-r
    words = ['with', 'and', 'for', 'the']
    fr_equivs = ['ù', 'ç', 'é', 'à', ]
    # lower case
    for i, w in enumerate(words):
        text = text.replace(w, fr_equivs[i])
    for i, w in enumerate(words):
        text = text.replace(w.upper(), fr_equivs[i].upper())
    for i, w in enumerate(words):
        text = text.replace(w.capitalize(), fr_equivs[i].upper())
    return text



####################################################
# These two incomplete helper functions are to help you get started

def convert_contractions(text):
    '''(str) -> str
    Convert English text so that both whole-word contractions
    and two-letter contractions are changed to the appropriate
    French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    Refer to the docstrings for whole_word_contractions and 
    two_letter_contractions for more info.

    >>> convert_contractions('with')
    'ù'
    >>> convert_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meœ'
    >>> convert_contractions('chat')
    'âat'
    >>> convert_contractions('wither')
    'ùï'
    >>> convert_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> convert_contractions('Showed The Neighbourhood Where')
    'Îœë À Neiêbürhood Ûïe'
    '''
    
    if ('with' in text.lower()):
        text = text.replace('with', whole_word_contractions('with'))
    if ('WITH' in text or 'With' in text):
        text = text.replace('WITH', whole_word_contractions('WITH'))
        text = text.replace('With', whole_word_contractions('With'))
    if ('and' in text.lower()):
        text = text.replace('and', whole_word_contractions('and'))
    if ('AND' in text or 'And' in text):
        text = text.replace('AND', whole_word_contractions('AND'))
        text = text.replace('And', whole_word_contractions('And')) 
    if ('for' in text.lower()):
        text = text.replace('for', whole_word_contractions('for'))
    if ('FOR' in text or 'For' in text):
        text = text.replace('FOR', whole_word_contractions('FOR'))
        text = text.replace('For', whole_word_contractions('For'))
    if ('the' in text.lower()):
        text = text.replace('the', whole_word_contractions('the'))
    if ('THE' in text or 'The' in text):
        text = text.replace('THE', whole_word_contractions('THE'))
        text = text.replace('The', whole_word_contractions('The'))
    
    text = two_letter_contractions(text)
    
    return text


def convert_quotes(text):
    '''(str) -> str
    Convert the straight quotation mark into open/close quotations.
    >>> convert_quotes('"Hello"')
    '“Hello”'
    >>> convert_quotes('"Hi" and "Hello"')
    '“Hi” and “Hello”'
    >>> convert_quotes('"')
    '“'
    >>> convert_quotes('"""')
    '“”“'
    >>> convert_quotes('" "o" "i" "')
    '“ ”o“ ”i“ ”'
    '''
    
    for i in range(int(text.count('"')/2+1)):
        text = text.replace( '"', '“', 1)
        text = text.replace( '"', '”', 1)
    
    return text 


####################################################
# Put your own helper functions here!

def number_to_english_braille(text):
    '''(str) -> str
    Converts numbers to English braille.
    >>> print_ostring(number_to_english_braille('0'))
    .o .o ..
    .o oo .o
    oo .. .o
    >>> print_ostring(number_to_english_braille('130'))
    .o o. oo .o ..
    .o .. .. oo .o
    oo .. .. .. .o
    '''
    text_in_braille = ''
    
    for i, char in enumerate(text):
        if (is_digit(text[i])):
            text_in_braille += ENG_NUMBER_START + '\n\n'
            break
        
    for char in text:
        if (is_digit(char)):
            text_in_braille += char_to_braille(char) + '\n\n'
            
    text_in_braille += ENG_NUMBER_END + '\n\n'
            
            
    return text_in_braille


def punctuation_to_english_braille(text):
    '''(str) -> str
    Convert punctuations to English braille.
    '''
    
    punc_in_eng_braille = ""
    
    for char in text:
        if (is_punctuation(char)):
            if (char in PUNCTUATION_ENG_1):
                punc_in_eng_braille += (decade_ending(0) + "\n" + decade_pattern(PUNCTUATION_ENG_1.find(char))) + '\n\n'
            elif (char in PUNCTUATION_ENG_2):
                punc_in_eng_braille += (decade_ending(0) + '\n' + decade_pattern(PUNCTUATION_ENG_2.find(char)+6)) + '\n\n'
            else:
                if (char == '?'):
                    punc_in_eng_braille += (decade_ending(0) + '\n' + decade_pattern(7)) + '\n\n'
                elif (char == '(' or char == ')'):
                    punc_in_eng_braille += (decade_ending(0) + '\n' + decade_pattern(6)) + '\n\n'
                elif (char == '!'):
                    punc_in_eng_braille += (decade_ending(0) + '\n' + decade_pattern(5)) + '\n\n'
                    
    return punc_in_eng_braille


####################################################

def english_text_to_braille(text):
    '''(str) -> str
    Convert text to English Braille. Text could contain new lines.

    This is a big problem, so think through how you will break it up
    into smaller parts and helper functions.
    Hints:
        - you'll want to call text_to_braille
        - you can alter the text that goes into text_to_braille
        - you can alter the text that comes out of text_to_braille
        - you shouldn't have to manually enter the Braille for 'and', 'ch', etc

    You are expected to write helper functions for this, and provide
    docstrings for them with comprehensive tests.

    >>> english_text_to_braille('202') # numbers
    '⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('2') # single digit
    '⠼⠃⠰'
    >>> english_text_to_braille('COMP') # all caps
    '⠠⠠⠉⠕⠍⠏'
    >>> english_text_to_braille('COMP 202') # combining number + all caps
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('and')
    '⠯'
    >>> english_text_to_braille('and And AND aNd')
    '⠯ ⠠⠯ ⠠⠯ ⠁⠠⠝⠙'
    >>> english_text_to_braille('chat that the with')
    '⠡⠁⠞ ⠹⠁⠞ ⠷ ⠾'
    >>> english_text_to_braille('hi?')
    '⠓⠊⠦'
    >>> english_text_to_braille('(hi)')
    '⠶⠓⠊⠶'
    >>> english_text_to_braille('"hi"')
    '⠦⠓⠊⠴'
    >>> english_text_to_braille('COMP 202 AND COMP 250')
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰ ⠠⠯ ⠠⠠⠉⠕⠍⠏ ⠼⠃⠑⠚⠰'
    >>> english_text_to_braille('For shapes with colour?')
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> english_text_to_braille('(Parenthetical)\\n\\n"Quotation"')
    '⠶⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠶\\n\\n⠦⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝⠴'
    '''
    # You may want to put code after this comment. You can also delete this comment. 



    # Here's a line we're giving you to get started: change text so the
    # contractions become the French accented letter that they correspond to
    text = convert_contractions(text)
    text = convert_quotes(text)
#    text = number_to_english_braille(text)
#    text = punctuation_to_english_braille(text)
    result = ""
    num = ""
    
    for char in text:
        if (not is_punctuation(char) or not is_digit(char)):
            result += text_to_braille(char)
        elif (is_punctuation(char)):
            result += ostring_to_unicode(char_to_braille(punctuation_to_english_braille(char)))
        elif (is_digit(char)):
            i = 0
            while (is_digit(text[text.find(char)+i])):
                num += char
                i+=1
            result += ostring_to_unicode(char_to_braille(number_to_english_braille(num)))
            num = ""
    
            

    # You may want to put code after this comment. You can also delete this comment.

    # Run the text through the French Braille translator
    #text = text_to_braille(text)

    # You may want to put code after this comment. You can also delete this comment.


    # Replace the French capital with the English capital
    result = result.replace(ostring_to_unicode(CAPITAL), ostring_to_unicode('..\n..\n.o'))

    

    return result


def english_file_to_braille(fname):
    '''(str) -> NoneType
    Given English text in a file with name fname in folder tests/,
    convert it into English Braille in Unicode.
    Save the result to fname + "_eng_braille".
    Provided to students. You shouldn't edit this function.

    >>> english_file_to_braille('test4.txt')
    >>> file_diff('tests/test4_eng_braille.txt', 'tests/expected4.txt')
    True
    >>> english_file_to_braille('test5.txt')
    >>> file_diff('tests/test5_eng_braille.txt', 'tests/expected5.txt')
    True
    >>> english_file_to_braille('test6.txt')
    >>> file_diff('tests/test6_eng_braille.txt', 'tests/expected6.txt')
    True
    '''  
    file_to_braille(fname, english_text_to_braille, "eng_braille")


if __name__ == '__main__':
    doctest.testmod()    # you may want to comment/uncomment along the way
    # and add tests down here
