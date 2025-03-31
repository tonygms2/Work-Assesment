import pandas as pd
import streamlit as st 
class VisualizeNetwork:
    def __init__(self,dataframe):
        self.df = dataframe
        st.set_page_config(page_title="Python Take-home Assessment Nicholas Tony Gomes")
    
    def showNetworksOnMap(self):
        st.subheader("Map")
        st.map(self.df, size = 20, color="#0044ff")
    
    def showNetworksAsGraph(self):
        st.subheader("Dataframe")
        st.write(self.df)

    def showBarchart(self):
        st.subheader("Bar Chart")
        st.bar_chart(self.df)