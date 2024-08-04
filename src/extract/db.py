from extract.api import call
import pandas as pd

def get_data(load_dt, movie_type={}):
    """
    Retrieves data based on specified load date and movie type.

    Args:
        load_dt (str): Load date in desired format (e.g., 'YYYY-MM-DD').
        movie_type (dict): Optional dictionary of movie type filters.
            Keys represent column names, values represent filter values.

    Returns:
        tuple: A tuple containing:
            - data (pd.DataFrame): DataFrame containing retrieved data with additional columns for load date and movie type filters.
            - partitions (list): List of column names used for partitioning the data.
    """
    top10 = call(dt=load_dt, url_param=movie_type)
    data = pd.DataFrame(top10)
    
    partitions = ['load_dt'] 
    data['load_dt'] = load_dt
    for k,v in movie_type.items():
        data[k] = v
        partitions = partitions + [k]
    
    return data, partitions