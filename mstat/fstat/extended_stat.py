import numpy
from functools import reduce

class ExtendedStat:

    @staticmethod
    def get_mnk(data):
        data = numpy.asarray(data, dtype='float64')
        n = len(data)
        xarray = [i for i in range(1, n + 1)]
        xy = map(lambda x, y: x * y, xarray, data)
        x2 = map(lambda x: x * x, data)

        summ_xy = reduce(lambda a, x: a + x, xy)
        summ_x = reduce(lambda a, x: a + x, xarray)
        summ_y = reduce(lambda a, x: a + x, data)
        summ_x2 = reduce(lambda a, x: a + x, x2)

        numerator = n * summ_xy - summ_x * summ_y
        denominator = n * summ_x2 - pow(summ_x, 2)

        a = numerator / denominator
        b = (summ_y - a * summ_x) / n

        return map(lambda x: a * x + b, xarray)