import argparse
import math

from artist import svg
from collections import namedtuple


__version__ = '0.1'

Line = namedtuple('Line', 'x1 x2 y1 y2 width color')

def main():
    parser = argparse.ArgumentParser(description='Draws an svg file.')
    parser.add_argument('file', help='The SVG file that gets output')
    parser.add_argument('source', help='The source to base the svg on')

    args = parser.parse_args()

    with svg.SvgFile(args.file) as svg_file:
        points = parse_file(args.source)
        print(len(points))
        svg_file.draw_path(points)
        

def fib(limit):
    lines = list()
    last = 0
    current = 1
    while True:
        next = current + last
        
        l = Line(current*2, next*2, next*2, current*2, 1, 'black')
        lines.append(l)

        last = current
        current = next

        if next > limit:
            break;

    return lines


def parse_file(path):
    with open(path, 'rb') as f:
        chars = f.read()

    points = list()
    for i in range(0, len(chars), 2):
        try:
            x = chars[i] * math.log(i)
            y = chars[i+1] * math.log(i)
            points.append(svg.Point(x, y))
        except:
            pass

    if len(points) > 10000:
        return points[::15]
    elif len(points) > 1000:
        return points[::8]
    else:
        return points
