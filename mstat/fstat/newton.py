# Newton interpolation method 1.0

class __Newton:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cache = {}
        self.a = []
        for i in range(len(x)):
            self.a.append(self.__f(0, i))
        self.cache = None
        self.y = None

    def __f(self, i, n):
        if (i, n) in self.cache.keys():
            return self.cache[(i, n)]
        result = 0
        if n == 0:
            result = self.y[i]
        else:
            result = (self.__f(i + 1, n - 1) - self.__f(i, n - 1)) / (self.x[i + n] - self.x[i])
        self.cache.update({(i, n): result})
        return result

    def interpolate(self, x):
        l = len(self.a)
        result = 0
        px = 1
        for i in range(l):
            result += self.a[i] * px
            px *= (x - self.x[i])
        return result


def get_newton_interpolation_function(x, y):
    interpolator = __Newton(x, y)
    return interpolator.interpolate
