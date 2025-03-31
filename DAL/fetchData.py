import requests
import pandas as pd
import streamlit as st 
class FetchData:
    def __init__(self,url):
        self.url = url
         
    @st.cache_data
    def getNetworks(_self):
        res = []
        try:
            response = requests.get(_self.url)
            data = response.json()
            networks = data.get("networks", [])

            for network in networks[:5]:
                network_id = network.get("id")
                network_name = network.get("name") 

                network_location = network.get("location", {})
                network_lat = network_location.get("latitude")
                network_long = network_location.get("longitude")
                network_city = network_location.get("city")
                network_country = network_location.get("country")
                res.append({
                    "id":network_id,
                    "name":network_name,
                    "latitude":network_lat,
                    "longitude":network_long,
                    "city":network_city,
                    "country":network_country,
                    #"station_count":_self.getStationCount(network_id)
                })
            return pd.DataFrame(res)
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame([])  # return empty DataFrame on failure

        
    
    #function to get the station count from the url
    def getStationCount(_self, network_id):
        try:
            station_url = f"{_self.url}/{network_id}"
            response = requests.get(station_url)
            data = response.json()
            stations = data.get("network", {})
            station_count = stations.get("stations", [])
            return len(station_count)
        except Exception as e:
            print(f"Error fetching stations for {network_id}: {e}")
            return 0
