import os
import xml.etree.ElementTree as ET


class SvgFile(object):
    """
    Represents an SVG File.
    """

    def __init__(self, path):
        """
        Creates a new SVG file
        Implements a Context Manager
        """
        self.path = path

    def __enter__(self):
        self._initialize()
        return self

    def __exit__(self, type, value, traceback):
        self.svg_file.write("</svg>")
        self.svg_file.close()

    def _initialize(self):
        self.svg_file = open(self.path, 'w')
        self.svg_file.write('<svg xmlns="http://www.w3.org/2000/svg">\n')

    def draw_line(self, line):
        x1 = f'x1="{line.x1}"'
        x2 = f'x2="{line.x2}"'
        y1 = f'y1="{line.y1}"'
        y2 = f'y2="{line.y2}"'
        width = f'stroke-width="{line.width}"'
        color = f'stroke="{line.color}"'

        line_svg = f'\t<line {x1} {y1} {x2} {y2} {width} {color} />\n'
        self.svg_file.write(line_svg)

    def draw_path(self, points):
        self.svg_file.write(f'\t<path d="M{points[0].x} {points[1].y} ')
        for point in points:
            self.svg_file.write(f'L {point.x} {point.y} ')

        self.svg_file.write('Z" fill="transparent" stroke="black" />\n')

        
class Line(object):
    """
    Represent a line in an SVG file
    """
    def __init__(self, x1, x2, y1, y2, width, color):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.width = width
        self.color = color

class Point(object):
    """
    Represents a point in an SVG path
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
