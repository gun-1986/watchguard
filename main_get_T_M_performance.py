"""
Getting T and M series  performance of WatchGuard  Firewall
"""

from selenium import webdriver
from api.wgldnet.modeldata import ModelData
from api.wgldnet.dataframeprocess import DataFrameProcess

from conf.wgldnet import outconfig


__author__ = 'jin.qian'


def main():
    """Get T/M series Model's performance and save to 'd:/result.csv'"""

    web = webdriver.Chrome()

    model_data_obj = ModelData(web)
    model_data_obj.open()
    tm_model = model_data_obj.get_series_model(['WatchGuard® Firebox M Series', 'WatchGuard Firebox T Series'])

    df = model_data_obj.get_multi_model_performance_result(web, tm_model)

    print('give series data:\n{df}'.format(df=df))

    df = DataFrameProcess(df).sort('Firewall Throughput')
    print('before of rename:\n{df}'.format(df=df))

    df = DataFrameProcess(df).modify_model('WatchGuard® Model', 'Model', ' *WatchGuard *Firebox® *| *WatchGuard® *Firebox *')
    df.to_csv(outconfig.performance_out_name.)

    web.close()

if __name__ == '__main__':
    main()


