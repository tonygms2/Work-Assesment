#Written by: Nicholas Tony Gomes
#Date : 31/03/25
#Entry point of the application. 

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

    st.set_page_config(
        page_title="City Bike Sharing Network Dashboard",
        layout="wide",
    )   
    st.header("City Bike Sharing Network Dashboard 🚲")
    #create an object to of the fetchData class from the DAL (Data access layer)
    fetchData = FetchData(BASE_URL)
    df = pd.DataFrame(fetchData.getNetworks())
    #get the calculated mean stats for city and country from Dal and pass it in presentation layer
    stats_by_city,stats_by_country = fetchData.getSummaryStats(df)
    #pass the stats to presentation layer 
    visualizeData = VisualizeNetwork(df,stats_by_city,stats_by_country)

    #add metrics 
    visualizeData.showMetrics()
    
    #add piecharts
    visualizeData.showPieChart()

    #add maps
    visualizeData.showNetworksOnMap()
    
    #adding summary statistics
    visualizeData.showSummary()

    # visualizeData.showNetworksAsGraph()
    visualizeData.showBarchart()

    #adding a last footer
    visualizeData.addFooter()
    
    

if __name__ == "__main__":
    main()

#endregion