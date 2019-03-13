## this file contain several functions for data cleaning of the dataset

##
def credit_year(row):
    if pd.notna(row):
        ## find the year in string type document
        year_str = re.compile('\d{4}').findall(row.split(',')[-1])
        if year_str:
            year_int = int(year_str[0])
            ## filter wrong years according to the found year of the museum
            if 1870 <= year_int <= 2019:
                return pd.Timestamp(str(year_int))
    return np.nan
