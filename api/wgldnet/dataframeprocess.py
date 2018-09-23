import re
from common import dataunit


class DataFrameProcess(object):

    def __init__(self, df):
        self.df = df

    def sort(self, column_name):
        """Return pd.DataFrame after sort by column_name

        :param column_name: label of column name
        """
        sort_column = list(self.df.loc[:, column_name])
        print('sort column is:\n{sort_column}'.format(sort_column=sort_column))

        sort_column = dataunit.to_data(sort_column, {'Gbps': 10 ** 9, 'Mbps': 10 ** 6, 'Kbps': 10 ** 3, 'bps': 10 ** 0})
        self.df.insert(0, 'px999', sort_column)
        self.df = self.df.sort_values('px999')

        self.df = self.df.iloc[:, 1:]

        print('after sort of data:\n{df}'.format(df=self.df))
        return self.df


    def modify_model(self, old_name, new_name, del_substring_re):
        """Modify Model column of pd.DataFrame and return pd.DataFrame which can't contain 'WatchGuard *Firebox'"""
        self.df = self.df.reset_index()

        self.df.rename(columns={old_name: new_name}, inplace=True)

        model = list(self.df.loc[:,new_name])
        model = list(map(lambda x: re.sub(del_substring_re, '', x), model))

        self.df.update({new_name: model})

        self.df = self.df.set_index(new_name)

        print('after modify model:\n{df}'.format(df=self.df))
        return self.df