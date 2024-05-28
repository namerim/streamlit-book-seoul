# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:06:24 2024

@author: 213
"""

import pandas as pd

def load_data() :
    data = pd.read_csv('seoul_real_estate_10000.csv')
    return data