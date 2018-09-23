"""
Config file of performance data, e.g.:
https://www.watchguard.com/wgrd-products/appliances-compare/15016/26071/15031

Need config row of table data, it's start with 1 but not 0
"""

table = '//*[@id="block-system-main"]/div/table/tbody'
page = 'https://www.watchguard.com/wgrd-products/appliances-compare/15016/26071/15031'
head_row = 2
data_row = range(13, 18)
