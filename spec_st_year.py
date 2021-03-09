def get_st_data(year_list, stname_list):
    '''Enter a list of the desired years and street name (as a list of strings) to download the traffic flow count
    data for that year. Example: enter '7' for the year 2007. Make sure to enter a list even if only requesting a single 
    year or street name.'''
    all_data = gpd.GeoDataFrame()
    for i in range(len(year_list)):
        year = year_list[i]
        gdf_year = get_gdf(year)
        all_data = all_data.append(gdf_year)
    st_data_year = gpd.GeoDataFrame()
    for j in range(len(stname_list)):
        st_data_year = st_data_year.append(all_data.loc[all_data['STNAME'] == stname_list[j]])
    return st_data_year
