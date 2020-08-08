import all_rolls

def markdown_filename(x, y):
    return 'x.{0:+}.y.{1:+}.md'.format(x, y)
    
def format_link(hex):
    if all_rolls.sizes['minX'] < hex.x < all_rolls.sizes['maxX'] and all_rolls.sizes['minY'] < hex.y < all_rolls.sizes['maxY']:
        return '[x{0:+}y{1:+}](x.{0:+}.y.{1:+}.md#top)'.format(hex.x, hex.y)
    return 'x{0:+}y{1:+}'.format(hex.x, hex.y)

def format_img(hex):
    return '![x{0:+}y{1:+}](images/x.{0:+}.y.{1:+}.png)'.format(hex.x, hex.y)

def format_describe(hex):
    color = hex.sync_roll('settlement', 'color')
    mascot = hex.sync_roll('settlement.mascot', 'predator')
    culture = hex.sync_roll('settlement', 'culture')
    demihuman = hex.sync_roll('settlement', 'demihuman')
    settlement = hex.sync_roll('settlement', 'settlement')
    return f'{demihuman} {settlement} (_{color}, {culture}, {mascot}_)'