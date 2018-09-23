"""
This module solves the problem of  operating web element, Make processing simpler.
"""

from lib.web.webretry import WebMeta

__author__ = 'jin.qian'


class WebUnit(metaclass=WebMeta):
    """
     Operate web element by xpath, like set, get, click
    """
    
    def __init__(self, web):
        self.web = web

    def open(self, page):
        self.web.get(page)

    def page_check(self):
        print("check web page")
        page = self.web.page_source
        if "main-frame-error" in page:
            print("web return error!!!")
            self.web.get(self.web.current_url)
            raise Exception("web return error!!!")

    def set(self, xpath, value):
        if self.web.find_element_by_xpath(xpath).tag_name == 'select':
            alloptions = self.web.find_element_by_xpath(xpath).find_elements_by_tag_name("option")
            allvalues = map(lambda x: x.text, alloptions)
            d = dict(zip(allvalues, alloptions))

            d.get(value.strip()).click()

    def get_options(self, xpath):
        if self.web.find_element_by_xpath(xpath).tag_name == 'select':
            options = self.web.find_element_by_xpath(xpath).find_elements_by_tag_name("option")
            texts = list(map(lambda x: x.text.strip, options))
        return texts

    def get_options_dict(self, xpath):
        options_dict = {}
        print('xpath is "{xpath}"'.format(xpath=xpath))
        if self.web.find_element_by_xpath(xpath).tag_name == 'select':
            options_groups = self.web.find_element_by_xpath(xpath).find_elements_by_tag_name('optgroup')
            
            for group in options_groups:
                group_name = group.get_attribute('label')
                options = group.find_elements_by_tag_name("option")
                texts = list(map(lambda x: x.text.strip(),options))
                texts = options_dict.get(group_name, [])+texts
                
                if texts is not []:
                    options_dict.update({group_name: texts})
        print('Options dict is "{options_dict}"'.format(options_dict=options_dict))

        return options_dict

    def get(self, xpath):
        if self.web.find_element_by_xpath(xpath).tag_name == 'select':
            options = self.web.find_element_by_xpath(xpath).find_elements_by_tag_name("option")
            values = map(lambda x: x.get_attribute('value'), options)
            texts = list(map(lambda x: x.text, options))
            value = self.web.find_element_by_xpath(xpath).get_attribute('value')
            d = dict(zip(values, texts))
            return d.get(value)

    def click(self, xpath):
        self.web.find_element_by_xpath(xpath).click()


