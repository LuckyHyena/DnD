
import random
from pathlib import Path
from string import printable
import all_rolls

def map_over_map(sizes, f):
    for y in range(sizes['minY'], sizes['maxY']):
        for x in range(sizes['minX'], sizes['maxX']):
            f(x, y)

def hex_key(x, y):
    return f'x{x}y{y}'

def clean(s):
    return "".join(c for c in s.strip() if c in printable)

def NW(hex):
    return HexRolls(hex.x - 1, hex.y)

def N(hex):
    return HexRolls(hex.x, hex.y - 1)

def NE(hex):
    return HexRolls(hex.x + 1, hex.y - 1)

def W(hex):
    if hex.x % 2 == 0: return HexRolls(hex.x - 1, hex.y)
    else: return HexRolls(hex.x - 1, hex.y + 1)

def E(hex):
    if hex.x % 2 == 0: return HexRolls(hex.x + 1, hex.y - 1)
    else: return HexRolls(hex.x + 1, hex.y)

def SW(hex):
    return HexRolls(hex.x - 1, hex.y + 1)

def S(hex):
    return HexRolls(hex.x, hex.y + 1)

def SE(hex):
    return HexRolls(hex.x + 1, hex.y)

class Printer:
    def __init__(self, fp=None):
        self.fp = fp
    
    def print(self, msg=""):
        print(msg, file=self.fp)

class NotPrinter:
    def print(self, msg=""):
        pass

class HexRolls:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.key = hex_key(x, y)
    
    def my_rolls(self):
        if self.key not in all_rolls.the():
            all_rolls.the()[self.key] = {}
        return all_rolls.the()[self.key]

    def roll_a(self, category):
        first_options = list(Path("etc", "lists", category).iterdir())
        first_choice = random.randrange(len(first_options))

        result = first_options[first_choice]

        second_options = None
        second_choice = None
        with result.open() as suboptions:
            second_options = list(clean(f) for f in suboptions)

        if second_options is not None and any(len(x) > 0 for x in second_options):
            second_choice = random.randrange(len(second_options))
            result = second_options[second_choice]
        
        if type(result) != str:
            result = result.stem
        
        return dict(result=result, rolls=(first_choice, second_choice))
    
    def sync_roll(self, key, category):
        key = key + '.' + category
        r = self.my_rolls()
        if key not in r:
            r[key] = self.roll_a(category)
        return r[key]['result'].replace('_', ' ')

