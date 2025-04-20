# database

# at some point, I would love to transition this into a .db file
# and use sqlite3 to access it or something similar

pitches = [0,1,2,3,4,5,6,7,8,9,10,11] # 0 is C, 1 is C#, ... 11 is B

chord_dictionary = { # same as above
    "major": [0, 4, 7],
    "minor": [0, 3, 7],
    "5": [0, 7],
    "6": [0, 4, 7, 9],
    "m6": [0, 3, 7, 9],
    "7": [0, 4, 7, 10],
    "m7": [0, 3, 7, 10],
    "maj7": [0, 4, 7, 11],
    "dim": [0, 3, 6],
    "dim7": [0, 3, 6, 9],
    "half-dim7": [0, 3, 6, 10],
    "sus2": [0, 2, 7],
    "sus4": [0, 5, 7]
    }

scales = {
    "major": [0, 2, 4, 5, 7, 9, 11],
    "minor": [0, 2, 3, 5, 7, 8, 10],
    "harmonic minor": [0, 2, 3, 5, 7, 8, 11],
    "melodic minor": [0, 2, 3, 5, 7, 9, 11],
    "lydian": [0, 2, 4, 6, 7, 9, 11],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "dorian": [0, 2, 3, 5, 7, 9, 10],
    "phrygian": [0, 1, 3, 5, 7, 8, 10],
    "locrian": [0, 1, 3, 5, 6, 8, 10],
    "harmonic major": [0, 2, 4, 5, 7, 8, 11],
    "double harmonic major": [0, 1, 4, 5, 7, 8, 11],
    "neapolitan major": [0, 1, 3, 5, 7, 9, 11]
    }

diatonic_chords = {
    'major': [(0, 4, 7), (2, 5, 9), (4, 7, 11), (5, 9, 0), (7, 11, 2), (9, 0, 4), (11, 2, 5)], 
    'minor': [(0, 3, 7), (2, 5, 8), (3, 7, 10), (5, 8, 0), (7, 10, 2), (8, 0, 3), (10, 2, 5)], 
    'harmonic minor': [(0, 3, 7), (2, 5, 8), (3, 7, 11), (5, 8, 0), (7, 11, 2), (8, 0, 3), (11, 2, 5)], 
    'melodic minor': [(0, 3, 7), (2, 5, 9), (3, 7, 11), (5, 9, 0), (7, 11, 2), (9, 0, 3), (11, 2, 5)], 
    'lydian': [(0, 4, 7), (2, 6, 9), (4, 7, 11), (6, 9, 0), (7, 11, 2), (9, 0, 4), (11, 2, 6)], 
    'mixolydian': [(0, 4, 7), (2, 5, 9), (4, 7, 10), (5, 9, 0), (7, 10, 2), (9, 0, 4), (10, 2, 5)], 
    'dorian': [(0, 3, 7), (2, 5, 9), (3, 7, 10), (5, 9, 0), (7, 10, 2), (9, 0, 3), (10, 2, 5)], 
    'phrygian': [(0, 3, 7), (1, 5, 8), (3, 7, 10), (5, 8, 0), (7, 10, 1), (8, 0, 3), (10, 1, 5)], 
    'locrian': [(0, 3, 6), (1, 5, 8), (3, 6, 10), (5, 8, 0), (6, 10, 1), (8, 0, 3), (10, 1, 5)], 
    'harmonic major': [(0, 4, 7), (2, 5, 8), (4, 7, 11), (5, 8, 0), (7, 11, 2), (8, 0, 4), (11, 2, 5)], 
    'double harmonic major': [(0, 4, 7), (1, 5, 8), (4, 7, 11), (5, 8, 0), (7, 11, 1), (8, 0, 4), (11, 1, 5)], 
    'neapolitan major': [(0, 3, 7), (1, 5, 9), (3, 7, 11), (5, 9, 0), (7, 11, 1), (9, 0, 3), (11, 1, 5)]
    }

diatonic_7th_chords = {
    'major': [(0, 4, 7, 11), (2, 5, 9, 0), (4, 7, 11, 2), (5, 9, 0, 4), (7, 11, 2, 5), (9, 0, 4, 7), (11, 2, 5, 9)], 
    'minor': [(0, 3, 7, 10), (2, 5, 8, 0), (3, 7, 10, 2), (5, 8, 0, 3), (7, 10, 2, 5), (8, 0, 3, 7), (10, 2, 5, 8)], 
    'harmonic minor': [(0, 3, 7, 11), (2, 5, 8, 0), (3, 7, 11, 2), (5, 8, 0, 3), (7, 11, 2, 5), (8, 0, 3, 7), (11, 2, 5, 8)], 
    'melodic minor': [(0, 3, 7, 11), (2, 5, 9, 0), (3, 7, 11, 2), (5, 9, 0, 3), (7, 11, 2, 5), (9, 0, 3, 7), (11, 2, 5, 9)], 
    'lydian': [(0, 4, 7, 11), (2, 6, 9, 0), (4, 7, 11, 2), (6, 9, 0, 4), (7, 11, 2, 6), (9, 0, 4, 7), (11, 2, 6, 9)], 
    'mixolydian': [(0, 4, 7, 10), (2, 5, 9, 0), (4, 7, 10, 2), (5, 9, 0, 4), (7, 10, 2, 5), (9, 0, 4, 7), (10, 2, 5, 9)], 
    'dorian': [(0, 3, 7, 10), (2, 5, 9, 0), (3, 7, 10, 2), (5, 9, 0, 3), (7, 10, 2, 5), (9, 0, 3, 7), (10, 2, 5, 9)], 
    'phrygian': [(0, 3, 7, 10), (1, 5, 8, 0), (3, 7, 10, 1), (5, 8, 0, 3), (7, 10, 1, 5), (8, 0, 3, 7), (10, 1, 5, 8)], 
    'locrian': [(0, 3, 6, 10), (1, 5, 8, 0), (3, 6, 10, 1), (5, 8, 0, 3), (6, 10, 1, 5), (8, 0, 3, 6), (10, 1, 5, 8)], 
    'harmonic major': [(0, 4, 7, 11), (2, 5, 8, 0), (4, 7, 11, 2), (5, 8, 0, 4), (7, 11, 2, 5), (8, 0, 4, 7), (11, 2, 5, 8)], 
    'double harmonic major': [(0, 4, 7, 11), (1, 5, 8, 0), (4, 7, 11, 1), (5, 8, 0, 4), (7, 11, 1, 5), (8, 0, 4, 7), (11, 1, 5, 8)], 
    'neapolitan major': [(0, 3, 7, 11), (1, 5, 9, 0), (3, 7, 11, 1), (5, 9, 0, 3), (7, 11, 1, 5), (9, 0, 3, 7), (11, 1, 5, 9)]
    }

diatonic_qualities = {
    'major': ['major', 'minor', 'minor', 'major', 'major', 'minor', 'dim'], 
    'minor': ['minor', 'dim', 'major', 'minor', 'minor', 'major', 'major'], 
    'harmonic minor': ['minor', 'dim', 'other', 'minor', 'major', 'major', 'dim'], 
    'melodic minor': ['minor', 'minor', 'other', 'major', 'major', 'dim', 'dim'], 
    'lydian': ['major', 'major', 'minor', 'dim', 'major', 'minor', 'minor'], 
    'mixolydian': ['major', 'minor', 'dim', 'major', 'minor', 'minor', 'major'], 
    'dorian': ['minor', 'minor', 'major', 'major', 'minor', 'dim', 'major'], 
    'phrygian': ['minor', 'major', 'major', 'minor', 'dim', 'major', 'minor'], 
    'locrian': ['dim', 'major', 'minor', 'minor', 'major', 'major', 'minor'], 
    'harmonic major': ['major', 'dim', 'minor', 'minor', 'major', 'other', 'dim'], 
    'double harmonic major': ['major', 'major', 'minor', 'minor', 'other', 'other', 'other'], 
    'neapolitan major': ['minor', 'other', 'other', 'major', 'other', 'dim', 'other']
    }
	
diatonic_7th_qualities = {  
    'major': ['maj7', 'm7', 'm7', 'maj7', '7', 'm7', 'half-dim7'], 
    'minor': ['m7', 'half-dim7', 'maj7', 'm7', 'm7', 'maj7', '7'], 
    'harmonic minor': ['other', 'half-dim7', 'other', 'm7', '7', 'maj7', 'dim7'], 
    'melodic minor': ['other', 'm7', 'other', '7', '7', 'half-dim7', 'half-dim7'], 
    'lydian': ['maj7', '7', 'm7', 'half-dim7', 'maj7', 'm7', 'm7'], 
    'mixolydian': ['7', 'm7', 'half-dim7', 'maj7', 'm7', 'm7', 'maj7'], 
    'dorian': ['m7', 'm7', 'maj7', '7', 'm7', 'half-dim7', 'maj7'], 
    'phrygian': ['m7', 'maj7', '7', 'm7', 'half-dim7', 'maj7', 'm7'], 
    'locrian': ['half-dim7', 'maj7', 'm7', 'm7', 'maj7', '7', 'm7'], 
    'harmonic major': ['maj7', 'half-dim7', 'm7', 'other', '7', 'other', 'dim7'], 
    'double harmonic major': ['maj7', 'maj7', 'm6', 'other', 'other', 'other', 'other'], 
    'neapolitan major': ['other', 'other', 'other', '7', 'other', 'half-dim7', 'other']
    }

diatonic_triad_numerals = {
    'major': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'], 
    'minor': ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII'], 
    'harmonic minor': ['i', 'ii°', 'III', 'iv', 'V', 'VI', 'vii°'], # III
    'melodic minor': ['i', 'ii', 'III', 'IV', 'V', 'vi°', 'vii°'], # III
    'lydian': ['I', 'II', 'iii', 'iv°', 'V', 'vi', 'vii'], 
    'mixolydian': ['I', 'ii', 'iii°', 'IV', 'v', 'vi', 'VII'], 
    'dorian': ['i', 'ii', 'III', 'IV', 'v', 'vi°', 'VII'], 
    'phrygian': ['i', 'II', 'III', 'iv', 'v°', 'VI', 'vii'], 
    'locrian': ['i°', 'II', 'iii', 'iv', 'V', 'VI', 'vii'], 
    'harmonic major': ['I', 'ii°', 'iii', 'iv', 'V', (8, 0, 4), 'vii°'], 
    'double harmonic major': ['I', 'II', 'iii', 'iv', (7, 11, 1), (8, 0, 4), (11, 1, 5)], 
    'neapolitan major': ['i', (1, 5, 9), (3, 7, 11), 'IV', (7, 11, 1), 'vi°', (11, 1, 5)]
}

diatonic_7th_numerals = {
    'major': ['IM7', 'ii7', 'iii7', 'IVM7', 'V7', 'vi7', 'viiø7'], 
    'minor': ['i7', 'iiø7', 'IIIM7', 'iv7', 'v7', 'VIM7', 'VII7'], 
    'harmonic minor': ['i7', 'iiø7', 'IIIM7', 'iv7', 'V7', 'VIM7', 'vii°7'], #i7, IIIM7
    'melodic minor': ['i7', 'ii7', 'IIIM7', 'IV7', 'V7', 'viø7', 'viiø7'], #i7, IIIM7
    'lydian': ['IM7', 'II7', 'iii7', 'ivø7', 'VM7', 'vi7', 'vii7'], 
    'mixolydian': ['I7', 'ii7', 'iiiø7', 'IVM7', 'v7', 'vi7', 'VIIM7'], 
    'dorian': ['i7', 'ii7', 'IIIM7', 'IV7', 'v7', 'viø7', 'VIIM7'], 
    'phrygian': ['i7', 'IIM7', 'III7', 'iv7', 'vø7', 'VIM7', 'vii7'], 
    'locrian': ['iø7', 'IIM7', 'iii7', 'iv7', 'VM7', 'VI7', 'vii7'], 
    'harmonic major': ['IM7', 'iiø7', 'iii7', (5, 8, 0, 4), 'V7', (8, 0, 4, 7), 'vii°7'], 
    'double harmonic major': ['IM7', 'IIM7', (4, 7, 11, 1), (5, 8, 0, 4), (7, 11, 1, 5), (8, 0, 4, 7), (11, 1, 5, 8)], 
    'neapolitan major': [(0, 3, 7, 11), (1, 5, 9, 0), (3, 7, 11, 1), 'IV7', (7, 11, 1, 5), 'viø7', (11, 1, 5, 9)]
}

chord_functions = {
    'tonic': ['I', 'i', 'vi', 'VI', 'IV'],
    'prepredominant': ['vi', 'IV'], # can be followed by anything
    'predominant': ['IV7', 'ii', 'ii7', 'bII6', 'It+6', 'Fr+6', 'Ger+6'], # must be followed by a dominant
    'dominant': ['V', 'V7', 'vii°', 'viiø7']
}

chromatic_predominants = {
    'bII6': [(1, 5, 8), 5], # full chord, bass note
    'It+6': [(0, 6, 8), 8],
    'Fr+6': [(0, 2, 6, 8), 8],
    'Ger+6': [(0, 3, 6, 8), 8]
}