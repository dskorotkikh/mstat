from scipy.interpolate import interp1d
from numpy import isnan
from mstat.fstat.newton import get_newton_interpolation_function

class Interpolation:

    NEWTON_HEADER = "newton"

    @staticmethod
    def get_interpolation_function(x, y, method):
        if method == Interpolation.NEWTON_HEADER:
            return get_newton_interpolation_function(x, y)
        return interp1d(x, y, method)

    @staticmethod
    def __interpolate(data, method, interpoints):
        l = len(data)
        if l < 2:
            return None
        x = [i for i in range(l)]
        function = Interpolation.get_interpolation_function(x, data, method)
        return [function(i/(interpoints + 1)) for i in range((l - 1) * interpoints + l)]

    @staticmethod
    def __unpack_data(data):
        return [float(val) for val in data]

    @staticmethod
    def __check_nan(data):
        if True in isnan(data):
            for i in range(len(data)):
                data[i] = 0

    @staticmethod
    def interpolate_spline(data, interpoints):
        result = Interpolation.__unpack_data(Interpolation.__interpolate(data, 3, interpoints))
        return [round(val, 2) for val in result]

    @staticmethod
    def interpolate_linear(data, interpoints):
        result = Interpolation.__unpack_data(Interpolation.__interpolate(data, "linear", interpoints))
        return [round(val, 2) for val in result]

    @staticmethod
    def interpolate_newton(data, interpoints):
        result = Interpolation.__unpack_data(Interpolation.__interpolate(data, Interpolation.NEWTON_HEADER, interpoints))
        Interpolation.__check_nan(result)
        return [round(val, 2) for val in result]
