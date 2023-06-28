# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:34:59 2023

@author: Jacks

Mad libs Generator
"""

noun = input('Choose a noun: ')
p_noun = input('Choose a plural noun: ')
noun2 = input('Choose another noun: ')
place = input('Name a place: ')
adjective = input('Name an adjective: ')
noun3 = input('Choose another noun: ')

print('-------------------------------------')
print('Be kind to your', noun + '-footed', p_noun)
print('For a duck may be somebody\'s', noun2 + ',')
print('Be kind to your', p_noun, 'in', place)
print('Where the weather is always', adjective + '. \n')
print('You may think that this is the', noun3 + ',')
print('Well, it is')
print('-------------------------------------')