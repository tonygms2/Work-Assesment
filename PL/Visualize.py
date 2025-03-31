import streamlit as st 
import altair as alt
import Helper.helper as hlp
import pycountry

class VisualizeNetwork:
    def __init__(self,dataframe,stat_by_city,stat_by_country):
        self.df = dataframe
        self.stat_by_city = stat_by_city
        self.stat_by_country = stat_by_country
       
    def showNetworksOnMap(self):
        st.subheader("Map Distribution")
        st.map(data=self.df,zoom=2, size=500, color="#0044ff")
    
    def showNetworksAsGraph(self):
        st.subheader("Dataframe")
        st.write(self.df)

    def showBarchart(self):
        st.subheader("Station Count by Network")
        
        # using altair chart here and we will pass it into st.altair_chart
        chart = alt.Chart(self.df).mark_bar().encode(
            x = alt.X('station_count', title="Number of Stations"),
            y = alt.Y('name:N', sort='-x', title="Network Name"),
            tooltip=['name','station_count']
        ).properties(height=400)

        st.altair_chart(chart,use_container_width=True)

    #showing mean stations per city and stations per country
    def showSummary(self):
        st.header("Summary Statistics")
        
        #create 2 columns layout and use with keyword so that columns values are accepted before components are re-ran
        col1,col2 = st.columns(2,vertical_alignment="top")
        with col1:
            st.subheader("Average Stations per City")
            st.dataframe(self.stat_by_city,hide_index=True)
        with col2:
            st.subheader("Average Stations per Country")
            st.dataframe(self.stat_by_country,hide_index=True)
        
    def showMetrics(self):
        st.header("Top Stats")
        #len returns the total number of rows from the dataframe
        total_networks = len(self.df)
        #get the top index of the top country with station_count of the dataframe
        top_country = self.df.groupby("country")["station_count"].sum().idxmax()
        top_country_full_name = hlp.get_country_name(top_country)

        top_country_count = self.df.groupby("country")["station_count"].sum().max()

        top_network = self.df.loc[self.df["station_count"].idxmax()]

        top_network_name = top_network["name"]
        top_network_count = top_network["station_count"]

        #get the 3 values from the streamlit columns
        column1, column2, column3 = st.columns(3)
        
        column1.metric("Total Networks", total_networks)
        column2.metric("Top Country (Most Stations)",f"({top_country_full_name}) {top_country}",f"{top_country_count} stations")
        column3.metric("Top Network (Most Stations)",f"{top_network_name}",f"{top_network_count} stations")
    
    def showPieChart(self):
        st.subheader("Network Distribution by Country")

        # Group by country and count the number of networks per country
        country_counts = self.df.groupby("country").size().reset_index(name='count')

        #  Map country codes to full names
        country_counts["country_full"] = country_counts["country"].apply(
            lambda code: pycountry.countries.get(alpha_2=code).name if pycountry.countries.get(alpha_2=code) else code
        )

        # Altair pie chart
        chart = alt.Chart(country_counts).mark_arc(innerRadius=45).encode(
            theta=alt.Theta(field="count", type="quantitative"),
            color=alt.Color(field="country_full", type="nominal"),
            tooltip=["country_full", "count"]
        ).properties(width=400, height=400)

        st.altair_chart(chart, use_container_width=True)
    

    def addFooter(self):
        footer_html = """<div style='text-align: center;'>
  <p>Built by Nicholas Tony Gomes  </p>
  <a href="https://github.com/tonygms2/Work-Assesment" target="_blank">Git Repo</a>
</div>"""
        st.markdown(footer_html, unsafe_allow_html=True)
