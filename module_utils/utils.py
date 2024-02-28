import pandas as pd
import numpy as np
import re
from datetime import datetime
import string  # for string generation
from functools import wraps

class Constants:
    QUANTILES = [0.01, 0.03, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.97, 0.99]
    

def time_it(func, *args):
    '''
    Wrapper func that Returns time to execute a function in seconds
    '''
    @wraps(func)
    def call_func(*args):
        start_time = datetime.now()
        val = func(*args)
        end_time = datetime.now()
        exec_time = (end_time - start_time).total_seconds()
        print(f'{str(func.__name__)} :: time taken to execute: {exec_time:.4f} seconds')
        return val
    return call_func

def filterData(df_raw:pd.DataFrame, dict_filter:dict)->pd.DataFrame:
    '''
    Filter the data wrt the dict {col: filter_criterion} that is passed.
    This also includes 'ALL' in the filter.
    Return back a filtered df.
    '''
    df = df_raw.copy()
    for k, v in dict_filter.items():
        if v=='ALL':
            continue
        filt = (df[k]==v)
        df = df.loc[filt,:]
    return df

@time_it
def write_data_to_file(df, path_filename:str, flag_write=False):
    file_ext = path_filename.split('.')[-1]  # check if parquet or csv
    if not flag_write:
        print(f'df will be written as {file_ext} to:\n{path_filename}\nChange `flag_write` to True to write data.')
    if flag_write:
        if file_ext=='csv':
            df.to_csv(path_filename, index=False)
        else: # assuming file extension other than csv to be parquet
            df.to_parquet(path_filename)
        print(f'df is written as {file_ext} to:\n{path_filename}')


