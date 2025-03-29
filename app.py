#region
# fetching the url with request library and store the data as pandas dataframe
import requests
import pandas as pd
import json as js

BASE_URL = "http://api.citybik.es/v2/networks"


def getNetworks(url):
    res = []
    try:
        response = requests.get(url)
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
        return js.dumps(res)

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


#fetching the url with request and wrapping it in try except block to handle errors
# and store the data as pandas dataframe
# try:
#     response = requests.get(BASE_URL)
#     data = response.json()
#     networks = data.get("networks", [])

#     for network in networks[:5]:
#         # Print the network ID and name
#         network_id = network.get("id")
#         network_name = network.get("name") 
#         network_location = network.get("location", {}) #get the location object and store as a dictionary       
# except requests.exceptions.RequestException as e:
#     print(f"Error fetching data: {e}")


#endregion


#region

def main():

    dataframe = getNetworks(BASE_URL)
    print(dataframe)
    # print(dataframe.head())

    # if  dataframe.empty:
    #     print("No networks found.")
    #     return
    
    
if __name__ == "__main__":
    main()

#endregion