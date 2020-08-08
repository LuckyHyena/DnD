from links import format_link as link, format_img as img, format_describe as describe
from hex2 import NW, N, NE, W, E, SW, S, SE

def render(p, hex):
    color = hex.sync_roll('settlement', 'color')
    mascot = hex.sync_roll('settlement.mascot', 'predator')
    culture = hex.sync_roll('settlement', 'culture')
    demihuman = hex.sync_roll('settlement', 'demihuman')
    settlement = hex.sync_roll('settlement', 'settlement')
    history = hex.sync_roll('settlement', 'history')

    resource = hex.sync_roll('environment', 'resource')
    water = hex.sync_roll('environment', 'water')
    underground = hex.sync_roll('environment', 'underground')
    highground = hex.sync_roll('environment', 'high_ground')

    plant = hex.sync_roll('environment', 'plant')
    plant_feature = hex.sync_roll('plant', 'creature_property')

    prey = hex.sync_roll('environment', 'prey')    
    prey_feature = hex.sync_roll('prey', 'creature_property')

    predator = hex.sync_roll('environment', 'predator')
    predator_feature = hex.sync_roll('predator', 'creature_property')

    villain = hex.sync_roll('problems', 'villain')
    
    ruin_color = hex.sync_roll('ruin', 'color')
    ruin_mascot = hex.sync_roll('ruin.mascot', 'predator')
    ruin_culture = hex.sync_roll('ruin', 'culture')
    ruin_demihuman = hex.sync_roll('ruin', 'demihuman')
    ruin_settlement = hex.sync_roll('ruin', 'settlement')
    ruin_history = hex.sync_roll('ruin', 'history')
    ruin_resource = hex.sync_roll('ruin', 'resource')
    ruin_predator = hex.sync_roll('ruin.current_inhabitant', 'predator')

    p.print()

    p.print('###### top')
    p.print(f'### Hex x{hex.x} y{hex.y}')
    p.print()
    p.print('|{0}|{0}|{0}|'.format('#' * 10))
    p.print('|-|-|-|')
    p.print(f'|**{link(NW(hex))}**|**{link(N(hex))}**|**{link(NE(hex))}**|')
    p.print(f'|{link(W(hex))}|**{img(hex)}**|{link(E(hex))}|')
    p.print(f'|**{link(SW(hex))}**|**{link(S(hex))}**|**{link(SE(hex))}**|')
    
    p.print()
    p.print('|{0}|{0}|{0}|'.format('#' * 10))
    p.print('|-|-|-|')
    p.print(f'|{describe(NW(hex))}|{describe(N(hex))}|{describe(NE(hex))}|')
    p.print(f'|-|**{describe(hex)}**|-|')
    p.print(f'|{describe(SW(hex))}|{describe(S(hex))}|{describe(SE(hex))}|')
    
    p.print()
    p.print(f'|Settlement|Area|Ruin|Creatures|')
    p.print(f'|-|-|-|-|')
    p.print(f'|{settlement}|{highground}|{ruin_settlement}|{predator}|')
    p.print(f'|{demihuman}|{water}|{ruin_demihuman}|{prey}|')
    p.print(f'|{resource}|{underground}|{ruin_culture}|{plant}|')
    p.print()
