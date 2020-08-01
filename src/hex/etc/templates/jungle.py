def render(p, hex):
    p.blank_line()
    with p.subhead('inhabitants') as sub:
        sub.label('settlement', hex.random('settlement'))
        sub.label('demihuman', hex.random('demihuman'))
        sub.label('resource', hex.random('resource'))
        with sub.subhead('society') as soc:
            soc.label('culture', hex.random('culture', key='settlement'))
            soc.label('history', hex.random('history', key='settlement'))
            soc.label('mascot animal', hex.random('predator', key='settlement'))

    p.blank_line()
    with p.subhead('area') as sub:
        sub.label('water', hex.random('water'))
        sub.label('high ground', hex.random('high_ground'))
        sub.label('underground', hex.random('underground'))
    
    p.blank_line()
    with p.subhead('environment') as sub:
        sub.label('villain', hex.random('villain'))
        sub.label('predator', "{1} {0}".format(hex.random('predator'), hex.random('creature_property', key='predator')))
        sub.label('prey', "{1} {0}".format(hex.random('prey'), hex.random('creature_property', key='prey')))
        sub.label('plant', "{1} {0}".format(hex.random('plant'), hex.random('creature_property', key='plant')))

    p.blank_line()
    with p.subhead('ruin') as sub:
        sub.label('settlement', hex.random('settlement', key='ruin'))
        sub.label('history', hex.random('history', key='ruin'))
        sub.label('current inhabitant', hex.random('predator', key='ruin'))
        with sub.subhead('builders') as two:
            two.label('builders', hex.random('demihuman', key='ruin'))
            two.label('culture', hex.random('culture', key='ruin'))
            two.label('resource', hex.random('resource', key='ruin'))
    
    p.blank_line()