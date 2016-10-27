import numpy


class BaseStat:

    @staticmethod
    def get_mean(data):
        return float(numpy.mean(data))

    @staticmethod
    def get_std(data):
        return float(numpy.std(data))

