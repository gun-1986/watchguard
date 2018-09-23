"""
This module solves the problem of  getting table element data of web
"""

__author__ = 'jin.qian'


class WebTable(object):
    """
    Getting table element data of web according to row number
    """
    web = None
    xpath = None
    
    def __init__(self, web,xpath):
        self.web = web
        self.xpath = xpath

    def table(self):
        """Return table instance of WebElement"""
        return self.web.find_element_by_xpath(self.xpath)

    def columns(self, row_num=1, tag_name='th'):
        """Return web table columns"""
        return len(self.table().find_element_by_xpath(self.xpath+'/tr['+str(row_num)+']').find_elements_by_tag_name(tag_name))
    
    def rows(self):
        """Return web table rows"""
        return len(self.table().find_element_by_xpath(self.xpath).find_elements_by_tag_name('tr'))

    def get_row_data(self, row_num=1, tag_name='td'):
        """Return web table row data"""
        tds = self.table().find_element_by_xpath(self.xpath+'/tr['+str(row_num)+']').find_elements_by_tag_name(tag_name)
        return list(map(lambda x: x.text.strip(),tds))

    def get_multi_row_data(self, row=[],tag_name='td'):
        """Return multiple rows data of web table"""
        result = []
        for i in row:
            result.append(self.get_row_data(i,tag_name))
        return result

    def get_head(self, row_num=1, tag_name='th'):
        """Return column name of web table"""
        return self.get_row_data(row_num, tag_name)
