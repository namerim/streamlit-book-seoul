# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:41:37 2024

@author: 213
"""

import streamlit as st
from streamlit_option_menu import option_menu
from utils import load_data
from home import run_home
from eda import run_eda_home

def main() :
    total_df = load_data()
    
    with st.sidebar:
        selected = option_menu('데시보드 메뉴', ['홈', '탐색적 자료분석', '부동산 예측'],
                               icons=['house', 'file-bar-graph', 'graph-up-arrow'], menu_icon='cast', default_index=0)
    
    if selected == '홈' :
        run_home(total_df)
    elif selected == '탐색적 자료분석' :
        run_eda_home(total_df)
    elif selected == '부동산 예측' :
        pass
    else :
        print('error')
        
if __name__ == "__main__" :
    main()
    
        
    