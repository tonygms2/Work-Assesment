#region
# fetching the url with request library and store the data as pandas dataframe
import requests
import pandas as pd
import json as js
from DAL.fetchData import FetchData
BASE_URL = "http://api.citybik.es/v2/networks"



#region commented
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
#endregion


#region

def main():
    #create an object to of the fetchData class from the DAL (Data access layer)
    fetchData = FetchData(BASE_URL)
    df = pd.DataFrame(fetchData.getNetworks())
    print(df.head())
    
if __name__ == "__main__":
    main()

#endregion