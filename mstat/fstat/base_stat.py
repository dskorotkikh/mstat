import numpy
from scipy import signal

class BaseStat:

    @staticmethod
    def get_mean(data):
        return float(numpy.mean(data))

    @staticmethod
    def get_std(data):
        return float(numpy.std(data))

    @staticmethod
    def get_autocorrelation(data):
        data = numpy.asarray(data, dtype='float64')
        result = signal.correlate(data, data, mode='full')
        result /= max(result)
        return result[result.size/2:].tolist()

