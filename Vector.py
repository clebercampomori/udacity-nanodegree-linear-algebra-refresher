import operator


class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates are required.')
        except TypeError:
            raise TypeError('The coordinates must be an iterable type.')

    def add(self, otherVector):
        return Vector(tuple(map(operator.add, self.coordinates, otherVector.coordinates)))

    def subtract(self, otherVector):
        return Vector(tuple(map(operator.sub, self.coordinates, otherVector.coordinates)))

    def scalar_multiply(self, factor):
        return Vector([v * factor for v in self.coordinates])

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, otherVector):
        return self.coordinates == otherVector.coordinates
