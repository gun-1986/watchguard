"""
Getting T and M series  performance of WatchGuard  Firewall
"""

from conf.wgldnet import compareselect
import pandas as pd
from selenium import webdriver
from api.wgldnet.modeldata import ModelData
from common import dataunit
import re

__author__ = 'jin.qian'


def get_multi_model_performance_result(web, model):
    """Return instance of pd.DataFrame which contains performance

        :param web: Instance of selenium.webdriver
        :param model: Model list of WatchGuard
    """
    df = pd.DataFrame()
    for i in range(0, len(model)//3+1):
        model_data = ModelData(web)
        model_data.open()
        print("model is {model}".format(model=model))
        model_data.select_model(compareselect.product1, model[i*3])
        
        if (i*3+1) == len(model):
            model_data.select_model(compareselect.product2, model[i*3])
        elif (i*3+1) <= (len(model)-1):
            model_data.select_model(compareselect.product2, model[i*3+1])
        
        if (i*3+2) <= (len(model)-1):
            model_data.select_model(compareselect.product3, model[i*3+2])
        
        model_data.exec_compare()
        
        df = df.append(model_data.get_performance_result())
        
    return df


def performance_sort(df, column):
    """Return pd.DataFrame after sort by column

    :param df: Instance of pd.DataFrame
    :param column: label of column name
    """
    sort_column = list(df.loc[:, column])
    print('sort column is:\n{sort_column}'.format(sort_column=sort_column))

    sort_column = dataunit.to_data(sort_column, {'Gbps': 10**9, 'Mbps': 10**6, 'Kbps': 10**3, 'bps': 10**0})
    df.insert(0, 'px999', sort_column)
    df = df.sort_values('px999')

    df = df.iloc[:, 1:]

    print('after sort of data:\n{df}'.format(df=df))
    return df


def modify_model(df):
    """Modify Model column of pd.DataFrame and return pd.DataFrame which can't contain 'WatchGuard *Firebox'"""
    df = df.reset_index()

    df.rename(columns={'WatchGuard® Model': 'Model'}, inplace=True)

    model = list(df.loc[:, 'Model'])
    model = list(map(lambda x: re.sub(' *WatchGuard *Firebox® *| *WatchGuard® *Firebox *', '', x), model))

    df.update({'Model': model})
    
    df = df.set_index('Model')

    print('after modify model:\n{df}'.format(df=df))
    return df


if __name__ == '__main__':
    """Get T/M series Model's performance and save to 'd:/result.csv'"""

    web = webdriver.Chrome()
    
    model_data = ModelData(web)
    model_data.open()

    model = model_data.get_series_model(['WatchGuard® Firebox M Series', 'WatchGuard Firebox T Series'])
    
    df = get_multi_model_performance_result(web, model)

    print('give series data:\n{df}'.format(df=df))  
    
    df = performance_sort(df, 'Firewall Throughput')
    print('before of rename:\n{df}'.format(df=df))
    
    df = modify_model(df)
    df.to_csv('d:/result.csv')
    
    web.close()


