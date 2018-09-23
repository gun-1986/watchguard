"""
Get model and performance from web
"""
from lib.web.webtable import WebTable
from lib.web.webunit import WebUnit
from conf.wgldnet import compareresult,compareselect
# import numpy as np
import pandas as pd

__author__ = 'jin.qian'


class ModelData(object):
    """
    Get Data from web
    """

    def __init__(self, web):
        """
        Constructor
        """        
        self.web = web
    
    def open(self, url=compareselect.page):
        WebUnit(self.web).open(url)

    def get_all_model(self, xpath=compareselect.product1):
        return WebUnit(self.web).get_options(xpath)
    
    def get_all_model_dict(self, xpath=compareselect.product1):
        return WebUnit(self.web).get_options_dict(xpath)

    def get_all_series(self, xpath=compareselect.product1):
        return list(self.get_all_model_dict(xpath).keys())
        
    def get_series_model(self, series_list=[], xpath=compareselect.product1):
        
        model_dict = self.get_all_model_dict(xpath)
        print("model_dict is {model_dict}".format(model_dict=model_dict))
        model = []
        print("series_list is {series_list}".format(series_list=series_list))
        for series in series_list:
            print("series is {series}".format(series=series))
            print("model_dict is {model_dict}".format(model_dict=model_dict))
            if series in model_dict:
                model.extend(model_dict.get(series))
        return model

    def select_model(self, xpath, model):
        WebUnit(self.web).set(xpath, model)
                                 
    def click(self, xpath=compareselect.submit):
        WebUnit(self.web).click(xpath)        
    
    def get_compare_result(self, table_xpath, head_row=1, data_row=[], contain_index=True, 
                           index_coloum=1, head_tag_name='th', data_tag_name='td', transpose=False):
        h = WebTable(self.web, table_xpath).get_head(2)
        print("head:{head}".format(head=h))
        data = WebTable(self.web, table_xpath).get_multi_row_data(range(13, 18))
        print("data:{data}".format(data=data))
        table_data = [h]+data
        print("table_data:{table_data}".format(table_data=table_data))
        df = pd.DataFrame(table_data)
        if transpose:
            df = df.T
            print('after T of df:\n {df}'.format(df=df))
            columns = list(df.iloc[index_coloum-1,])
            print('columns: {columns}'.format(columns=columns))
            index_key = columns[0]
            print('index_key: {index_key}'.format(index_key=index_key))
            df=df.iloc[1:]
            print('data of df:\n {df}'.format(df=df))
            df.columns = columns
            print('after set columns of df:\n {df}'.format(df=df))
            df = df.set_index(index_key)
            print('after set index of df:\n {df}'.format(df=df))
        else:
            pass
        return df
        
    def get_performance_result(self, table_xpath=compareresult.performance.table, 
                               head_row=compareresult.performance.head_row, 
                               data_row=compareresult.performance.data_row):
        return self.get_compare_result(table_xpath,head_row,data_row,transpose=True)

    def get_multi_model_performance_result(self, web, model):
        """Return instance of pd.DataFrame which contains performance

            :param web: Instance of selenium.webdriver
            :param model: Model list of WatchGuard
        """
        df = pd.DataFrame()
        for i in range(0, len(model) // 3 + 1):
            self.open()
            print("model is {model}".format(model=model))
            self.select_model(compareselect.product1, model[i * 3])

            if (i * 3 + 1) == len(model):
                self.select_model(compareselect.product2, model[i * 3])
            elif (i * 3 + 1) <= (len(model) - 1):
                self.select_model(compareselect.product2, model[i * 3 + 1])

            if (i * 3 + 2) <= (len(model) - 1):
                self.select_model(compareselect.product3, model[i * 3 + 2])

            self.click()

            df = df.append(self.get_performance_result())

        return df