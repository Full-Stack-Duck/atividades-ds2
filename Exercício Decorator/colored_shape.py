class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        r = getattr(self.shape, 'resize', None)
        if callable(r):
            r(factor)

    def __str__(self):
        return '%s has the color %s' % (str(self.shape), self.color)
