#!/usr/bin/python3

from pathlib import Path
import hex2
import hex_template
import links
import all_rolls
import json

Path("var", "map").mkdir(parents=True, exist_ok=True)

if __name__ == '__main__':
    try:
        all_rolls.load_from('var', 'saved_rolls.json')
        print('successfully loaded from var/saved_rolls.json')
    except FileNotFoundError:
        print('failed to load from var/saved_rolls.json')

    global lastY
    lastY = -100000
    def do_all_rolls(x, y):
        global lastY
        key = hex2.hex_key(x, y)
        hex_template.render(hex2.NotPrinter(), hex2.HexRolls(x, y))
        if y != lastY:
            lastY = y
            print('rolled', x, y)

    hex2.map_over_map(all_rolls.sizes, do_all_rolls)

    all_rolls.save_to('var', 'saved_rolls.json')

    def render_template(x, y):
        global lastY
        key = hex2.hex_key(x, y)
        with Path('var', 'map', links.markdown_filename(x, y)).open('w') as page:
            hex_template.render(hex2.Printer(fp=page), hex2.HexRolls(x, y))
            
        if y != lastY:
            lastY = y
            print('rendered', x, y)
        
    hex2.map_over_map(all_rolls.sizes, render_template)