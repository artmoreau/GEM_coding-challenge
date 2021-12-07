# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:40:00 2021

@author: Arthur-Pc
"""

import json

def load_data(filename) :
    
    '''
    Given a valid .json file in filename, extract and return the information :
        
    load : float
    price_gas : float
    price_kerosine : float
    price_co2 : float
    wind : int
    powerplants : list of dict
    '''
    
    with open(filename) as json_file: 
        payload = json.load(json_file)
    
    load = payload.get('load')
    fuels = payload.get('fuels')
    price_gas = fuels.get('gas(euro/MWh)')
    price_kerosine = fuels.get('kerosine(euro/MWh)')
    price_co2 = fuels.get('co2(euro/ton)')
    wind = fuels.get('wind(%)')
    powerplants = payload.get('powerplants')
    
    return load,price_gas,price_kerosine,price_co2,wind,powerplants