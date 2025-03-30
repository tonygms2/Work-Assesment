import requests
import pandas as pd
import json as js

class FetchData:
    def __init__(self,url):
        self.url = url
         

    def getNetworks(self):
        res = []
        try:
            response = requests.get(self.url)
            data = response.json()
            networks = data.get("networks", [])

            for network in networks:
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
                })
            return res

        except Exception as e:
            print(f"Error fetching data: {e}")
            return None