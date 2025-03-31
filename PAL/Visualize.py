import requests
import pandas as pd
import streamlit as st 
class VisualizeNetwork:
    def __init__(self,dataframe):
        self.df = dataframe
    
    def showStationsOnMap(self):
        st.map(self.df, size = 20, color="#0044ff")