#region Imports and contstants

# fetching the url with request library and store the data as pandas dataframe
import pandas as pd
import json as js
from DAL.FetchData import FetchData
from PL.Visualize import VisualizeNetwork
import streamlit as st
BASE_URL = "http://api.citybik.es/v2/networks"
#endregion


#region

def main():
    #create an object to of the fetchData class from the DAL (Data access layer)
    fetchData = FetchData(BASE_URL)
    df = pd.DataFrame(fetchData.getNetworks())
    
    visualizeData = VisualizeNetwork(df)
    #use streamlit map to pin the latitude and longitude
    visualizeData.showNetworksAsGraph()
    visualizeData.showBarchart()
    visualizeData.showNetworksOnMap()
if __name__ == "__main__":
    main()

#endregion