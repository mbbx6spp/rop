from opc.hue import hsvToRgb


class Art(object):

    description = "Slow transition of hues across the display"

    def __init__(self, matrix):
        self.base = 0

    def start(self, matrix):
        pass

    def refresh(self, matrix):
        self.base += 4
        h = matrix.height - 1

        for x in range(matrix.width):
            hue = ((self.base+32*x) % 1024)/1024.0
            for y in range(matrix.height):
                sat = min(1, 0.25 + (1.5*y)/h)
                val = min(1, 0.25 + (1.5*(h-y)/h))
                matrix.drawPixel(x, y, hsvToRgb(hue, sat, val))

    def interval(self):
        return 100
