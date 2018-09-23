"""
According to giving dict which contain unit and data, calc data and then return
"""

import re


def __single_data_transform(data_with_unit, unit_dict):


    m = re.match('([\d\.]*)(.*)', data_with_unit.strip())
    if m is not None:
        data = float(m.group(1).strip())
        unit = m.group(2).strip()
        if unit in unit_dict:
                data = data * unit_dict.get(unit)
        else:
            raise Exception("There is't {unit} in unit dict".format(unit=unit))
    else:
        raise Exception("{data_with_unit} is incorrect".format(data_with_unit=data_with_unit))

    return data


def to_data(data_with_unit, unit_dict):
    """Return float list

        :param data_with_unit: The type of Data  with unit is string or string list
        :param unit_dict: Tell how to process data
        :param case_sensitive: True if case sensitive, vice versa

        :Usage example::

            to_data(['3 Gbps', '40 Mbps'], {'Gbps': 10**9, 'Mbps': 10**6, 'Kbps': 10**3, 'bps': 10**0})
    """

    if isinstance(data_with_unit, int):
        result = __single_data_transform(data_with_unit, unit_dict)
    elif isinstance(data_with_unit,list):
        result = []
        for data_with_unit in data_with_unit:
            result.append(__single_data_transform(data_with_unit, unit_dict))
    else:
        raise Exception("The type of data_with_unit is incorrect.")

    return result