# Greening Shared Repository:

- This shared repository functions as a collaboration space for data cleaning for both UW Direct 21 Greening Seattle Teams. The first team is focused on predicting Seattle Traffic Trends, while the second is focused on Visualizing Seattle Traffic Trends, as well as outputs of a regression model seeking to predict future traffic patterns based on user inputs.

- Local-level traffic data is provided for the city of Seattle, as well as by the Washington State Department of Transportation. These data can be found at: https://www.seattle.gov/transportation/document-library/reports-and-studies as well as https://www.wsdot.wa.gov/mapsdata/tools/trafficplanningtrends.htm for state level data.

- The existance of copious amounts of public information for local traffic data for the city of Seattle creates challenges for interacting with the data, any project involves a large data cleaning component, which needs to occur before prediction or visualization. 

- Typically, interactions are managed within commercial GIS (Geographic Information System) software, such as ArcGis. Here we take a python based approach to download, extract, clean, visualize and predict local traffic data for the city of Seattle.  

- The Greening Seattle Team workflow involves a feedback loop between both teams. Both visualization and prediction sub-groups partipated in gathering publically available data from the Seattle government. Then the data was cleaned with a focus on breaking out the dataset for a series of different input features including number of cars, number of bike lanes. This data was partitioned into subgroups by Census Tract, which are discrete geographic units. They are the smallest geographic measure collected by the US Census Bureau, which are the rough equivalent of a neighborhood.  

- The city of Seattle itself can be subdivided into 131 Census Tracts. For purposes of traffic visualization the census tract works for a convenient aggregate to visualize city-level trends. 

### Overall use cases for Greening Seattle Shared Repository:
  1. Compilation of traffic and location based data, such as census tract data and street level data. 
	* _User:_ Developers of GreeningSeattle software
	* _Function:_ compile and clean data for predictions and visualizations
	* _Results:_ return compatible data 



### Key Files within the repository:


- environment: Environment file containing needed packages for data cleaning

- spec_st_year: Extracts street level traffic data for a specific street for a user input year.

- get_geodata: Extracts Traffic Data for a specific user input year.

- traffic_df: Downloads traffic data from Seattle.gov and enables user to extract all traffic data organized by zip code and year, or just yearly aggregate traffic flow data.

- GeoSegment_Partitioning: Example Jupyter Notebook that allows basic aggregation of traffic data by census track. 


### Important! Before using software, please check to make sure you have the following additional packages downloaded into your conda environment:

- asdf
- 	sdaf
- 	asdf



-More Information about individual use cases and each project can be found within Visualization and Prediction Repositiories for each individual team.
