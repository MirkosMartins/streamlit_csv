# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 08:18:56 2022

@author: mirkos
"""

import streamlit as st
import pandas as pd

dataset = pd.read_csv('./nomes.csv',sep=';',header=0,names=['Nome'])
st.write('Teste do uso de csv como armazenamento online.')
st.table(dataset)
st.text_input("Digite um novo nome para inserir:",key="novoNome")
st.text('Nome digitado: '+st.session_state.novoNome)
novoDF = pd.DataFrame([str(st.session_state.novoNome)],columns=dataset.columns)
dataset = pd.concat([dataset,novoDF])
if st.button('Salvar'):
    dataset.to_csv('./nomes.csv',sep=';',index=False)
    st.table(dataset)
    st.text('Inserindo os dados. Dataset size:'+str(len(dataset)))

