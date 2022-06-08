# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:18:56 2022

@author: mirkos
"""

import streamlit as st
import pandas as pd

dataset = pd.read_excel('./nomes.xlsx',header=0,names=['Nome'])
st.write('Teste do uso de csv como armazenamento online.')
st.table(dataset)
st.text_input("Digite um novo nome para inserir:",key="novoNome")
novo = pd.Series([str(st.session_state.novoNome)])
n = pd.DataFrame(novo,columns=['Nome'])
pd.concat([dataset,n])
if st.button('Salvar'):
    dataset.to_excel('./nomes.xlsx',index=False)
    st.text('Inserindo os dados. Dataset size:',len(dataset))

