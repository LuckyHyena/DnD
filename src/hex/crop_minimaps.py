#!/usr/bin/python3

import json
from pathlib import Path
import hex2
import sys
from subprocess import run, STDOUT
from etc.templates import github
import coord
import all_rolls

sizes = json.load(Path("etc", "hexmap.json").open())
window_radius_hex = 2
pointer_radius_px = 10
pointer_color = '#F0F'
pointer_stroke_width = 5

Path("var", "map", "images").mkdir(parents=True, exist_ok=True)

def oob(x, y):
    xFits = 0 <= x <= sizes['maxPixelX'] 
    yFits = 0 <= y <= sizes['maxPixelY']
    return not (xFits and yFits)

def crop_map(x, y):
    # figure out the precise spot to aim at
    X = x * sizes['pixelX'] + sizes['originX']
    Y = y * sizes['pixelY'] + sizes['originY'] + (x * sizes['halfPixelX'])

    # zoom out to show neighbor hexes
    W = sizes['pixelX'] * (1 + window_radius_hex * 2)
    H = sizes['pixelY'] * (1 + window_radius_hex * 2)
    X = X - (sizes['pixelX'] * window_radius_hex)
    Y = Y - (sizes['pixelY'] * window_radius_hex)
    
    circleX = int(W / 2)
    circleY = int(H / 2)

    infile = str(Path('etc', sizes['sourceImage']))
    outfile = str(Path('var', 'map', 'images', 'x.{0:+}.y.{1:+}.png'.format(x, y)))

    if oob(X, Y) or oob(X + W, Y + H):
        print('skipping', x, y)
        return

    arguments = ['gm', 'convert', infile,
        '-crop', '{0}x{1}+{2}+{3}'.format(int(W), int(H), int(X), int(Y)),
        '-fill', pointer_color,
        '-draw', 'rectangle 0,0 48,12',
        '-fill', 'black',
        '-draw', 'text 2,10 \'{0:+}{1:+}\''.format(x, y),
        '-stroke', pointer_color,
        '-fill', 'none',
        '-strokewidth', str(pointer_stroke_width),
        '-draw', 'circle {0},{1} {2},{3}'.format(int(circleX), int(circleY), int(circleX + pointer_radius_px), int(circleY + pointer_radius_px)),
    outfile]
    print(arguments)
    run(arguments, stdout=sys.stdout, stderr=sys.stderr)

if __name__ == "__main__":
    hex2.map_over_map(all_rolls.sizes, crop_map)