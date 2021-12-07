# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:41:13 2021

@author: Arthur-Pc
"""

import json

def write_response(powerplants, powers, filename):
    
    '''
    Given a list of powerplants in powerplants and the associated powers,
    write in 'response_'+filename+'.json' file the corresponding response.
    
    
    If the powers could not be computed, write an error message instead.
    '''
    
    if isinstance(powers,int) : #Il s'agit d'un code d'erreur
        # We can parse the integer in powers and adapte the message 
        json_message = {"error" : powers,
                        "message" : 'Solution is impossible to reach'}
    else :
        json_message =  [{"name" : powerplants[i].get('name'), "p" : powers[i]} for i in range(len(powerplants))]
    
    with open('response_' + filename, 'w') as file:
        json.dump(json_message, file)