from scipy.interpolate import interp1d

class Interpolation:

    @staticmethod
    def __interpolate(data, method, interpoints):
        l = len(data)
        if l < 2:
            return None
        x = [i for i in range(l)]
        function = interp1d(x, data, method)
        return [function(i/(interpoints + 1)) for i in range((l - 1) * interpoints + l)]

    @staticmethod
    def __unpack_data(data):
        return [float(val) for val in data]

    @staticmethod
    def interpolate_spline(data, interpoints):
        return Interpolation.__unpack_data(Interpolation.__interpolate(data, 1, interpoints))

    @staticmethod
    def interpolate_linear(data, interpoints):
        return Interpolation.__unpack_data(Interpolation.__interpolate(data, "linear", interpoints))
