# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 16:09:14 2021

@author: Arthur-Pc
"""

import sys
from load_data import load_data
from write_response import write_response
from algo import solver

def main(filename) : 

    load,price_gas,price_kerosine,price_co2,wind,powerplants = load_data(filename)
    powers = solver(load,powerplants,price_gas,price_co2,price_kerosine,wind)
    write_response(powerplants, powers,filename)
    
if __name__ == '__main__' :
    
    if len(sys.argv) == 1 : # No input argument
        print('Please enter a .json file as the first argument')
    else :
        main(sys.argv[1])