"""
use closure and metaclass, retry some operations
"""
import time


def retry(second_list):
    """
    :param second_list: After several seconds of sleep, try again. The maximum retry number is list length.
    :return:
    """
    def _retry(func):
        def __retry(*args, **kwargs):
            for i, t in enumerate(second_list):
                try:
                    print("{fun}({args}) retry {i}th times".
                          format(i=str(i), fun=func.__name__, args=str(list(args)[1:])[1:-1]))

                    time.sleep(t)
                    return func(*args, **kwargs)
                    break
                except Exception as e:
                    if i + 1 == len(second_list):
                        print("{fun}({args}) retry {i}th times".
                              format(i=str(i), fun=func.__name__, args=str(list(args)[1:])[1:-1]))

        return __retry

    return _retry


def add_page_check(func):
    def _add_page_check(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        finally:
            args[0].page_check()
    return _add_page_check


class WebMeta(type):

    def __new__(cls, class_name, class_parents, class_attr):
        for name, value in class_attr.items():
            if name in ['page_check', 'open']:
                class_attr[name] = retry([0.1, 0.1, 10, 10, 10])(value)
            elif '__' not in name:
                class_attr[name] = add_page_check(value)
        return type(class_name, class_parents, class_attr)
