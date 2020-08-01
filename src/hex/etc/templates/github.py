import json
from pathlib import Path

sizes = json.load(Path('etc', 'hexmap.json').open())

def print_links(p, hex):
    p.print('|{0}|{0}|{0}|'.format('#' * 10))
    p.print('|-|-|-|')
    p.print('|**{0}**|**{1}**|**{2}**|'.format(
        format_link(hex, -1, 0),
        format_link(hex, 0, -1),
        format_link(hex, +1, -1)
    ))
    p.print('|**{0}**|**{1}**|**{2}**|'.format(
        w_link(hex),
        format_img(hex, 0, 0),
        e_link(hex)
    ))
    p.print('|**{0}**|**{1}**|**{2}**|'.format(
        format_link(hex, -1, +1),
        format_link(hex, 0, +1),
        format_link(hex, +1, 0)
    ))

def w_link(hex):
    if hex.x % 2 == 0:
        return format_link(hex, -1, 0)
    else:
        return format_link(hex, -1, +1)

def e_link(hex):
    if hex.x % 2 == 0:
        return format_link(hex, +1, -1)
    else:
        return format_link(hex, +1, 0)

def format_table(hex, x, y):
    return '{0} {1}'.format(format_link(hex, x, y), format_img(hex, x, y))

def format_link(hex, x, y):
    X = hex.x + x
    Y = hex.y + y
    if sizes['minX'] < X < sizes['maxX'] and sizes['minY'] < Y < sizes['maxY']:
        return '[x{0:+}y{1:+}](x.{0:+}.y.{1:+}.md#top)'.format(X, Y)
    return 'x{0:+}y{1:+}'.format(X, Y)

def format_img(hex, x, y):
    return '![x{0:+}y{1:+}](images/x.{0:+}.y.{1:+}.png)'.format(hex.x + x, hex.y + y)

def render(p, hex):
    p.blank_line()
    p.print('###### top')
    p.print('### Hex X `{0}` Y `{1}`'.format(hex.x, hex.y))
    p.print('# {0} {1} {2}'.format(hex.random('culture', key='settlement'), hex.random('demihuman'), hex.random('settlement')))
    p.blank_line()
    print_links(p, hex)

    p.blank_line()
    p.print('# Inhabitants')
    p.label('+ Settlement', hex.random('settlement'))
    p.label('+ Demihuman', hex.random('demihuman'))
    p.label('+ Resource', hex.random('resource'))
    with p.subhead('### Society') as soc:
        soc.label('+ Culture', hex.random('culture', key='settlement'))
        soc.label('+ History', hex.random('history', key='settlement'))
        soc.label('+ Mascot animal', hex.random('predator', key='settlement'))

    p.blank_line()
    p.print('# Environment')
    p.label('+ Water', hex.random('water'))
    p.label('+ High ground', hex.random('high_ground'))
    p.label('+ Underground', hex.random('underground'))

    p.blank_line()
    p.print('# Problems')
    p.label('+ Villain', hex.random('villain'))
    p.label('+ Predator', "{1} {0}".format(hex.random('predator'), hex.random('creature_property', key='predator')))
    p.label('+ Prey', "{1} {0}".format(hex.random('prey'), hex.random('creature_property', key='prey')))
    p.label('+ Plant', "{1} {0}".format(hex.random('plant'), hex.random('creature_property', key='plant')))

    p.blank_line()
    p.print('# Ruin')
    p.label('+ Settlement', hex.random('settlement', key='ruin'))
    p.label('+ History', hex.random('history', key='ruin'))
    p.label('+ Current inhabitant', hex.random('predator', key='ruin'))
    with p.subhead('### Builders') as two:
        two.label('+ Builders', hex.random('demihuman', key='ruin'))
        two.label('+ Culture', hex.random('culture', key='ruin'))
        two.label('+ Resource', hex.random('resource', key='ruin'))
    
    p.blank_line()