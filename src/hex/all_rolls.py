import json
from pathlib import Path

sizes = json.load(Path('etc', 'hexmap.json').open())

globbb = {}
globbb['the'] = {}

def the():
    return globbb['the']

def load_from(*args):
    with Path(*args).open() as loader:
        globbb['the'] = json.load(loader)

def save_to(*args):
    with Path(*args).open('w') as saver:
        json.dump(globbb['the'], saver)