import logging
import sys
import time
from functools import wraps
import matplotlib.pyplot as plt
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def timed(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('basic_metric')
        logger.debug("started {}".format(func.__name__))
        t_start = time.time()
        result = func(*args, **kwargs)
        t_end = time.time()
        logger.debug("finished {} took :{}".format(func.__name__, (t_end - t_start) * 1000))
        return result
    return wrapper


def partial_image(index_of_output):
    def inner_function(func):
        @wraps(func)
        def wrapper(*args):
            cm = plt.get_cmap('gray')
            kw = {'cmap': cm, 'interpolation': 'none', 'origin': 'upper'}
            result = func(*args)
            if index_of_output<0:
                plt.imshow(result, **kw)
            else:
                plt.imshow(result[index_of_output], **kw)
            plt.title('partial result: {}'.format(func.__name__))
            plt.show()
            return result
        return wrapper
    return inner_function
