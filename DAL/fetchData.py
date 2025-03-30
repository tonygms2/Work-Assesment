import requests
import pandas as pd

class FetchData:
    def __init__(self,url):
        self.url = url
         

    def getNetworks(self):
        res = []
        try:
            response = requests.get(self.url)
            data = response.json()
            networks = data.get("networks", [])

            for network in networks[:10]:
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
                    "station_count":self.getStationCount(network_id)
                })
            return pd.DataFrame(res)
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
        
    
    #function to get the station count from the url
    def getStationCount(self, network_id):
        try:
            station_url = f"{self.url}/{network_id}"
            response = requests.get(station_url)
            data = response.json()
            stations = data.get("network", {})
            station_count = stations.get("stations", [])
            return len(station_count)
        except Exception as e:
            print(f"Error fetching stations for {network_id}: {e}")
            return 0
