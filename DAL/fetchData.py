import requests
import pandas as pd
import streamlit as st 
import pycountry

class FetchData:
    def __init__(self, url):
        self.url = url
         
    @st.cache_data
    def getNetworks(_self):
        res = []
        try:
            response = requests.get(_self.url)
            data = response.json()
            networks = data.get("networks", [])
            #calling 50 networks to for testing and to prevent rate limiting
            for network in networks[:50]:
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
                    # "station_count":random.randint(0, 99)
                    "station_count":_self.getStationCount(network_id)
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

    #function to process the dataframe to give statistics and groups 
    #by city and by country

    def getSummaryStats(_self,df): 
        stats_by_city = df.groupby("city")["station_count"].mean().reset_index().rename(columns={"station_count":"avg_stations"})
        by_country = df.groupby("country")["station_count"].mean().reset_index().rename(columns={"station_count":"avg_stations"})
        
        # Convert 2-letter codes to full names with (code)
        by_country["country"] = by_country["country"].apply(
            lambda code: f"{pycountry.countries.get(alpha_2=code).name} ({code})"
            if pycountry.countries.get(alpha_2=code) else code
        )
        return stats_by_city,by_country