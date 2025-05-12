#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file provides chord logic to ordering chords into a progression.
"""

import database as db
import random

class Sequence():

    def __init__(self, key, scale):
        self.key = key
        self.scale = scale
        self.indexes = []
        self.numerals = []
        self.pitches = []


    def generate_sequence(self, seq_length, seq_key = -1, seq_scale = "", extended = False):
        """Generates a sequence using the given parameters.
        Args:
            seq_length(int): length of the sequence
            key(int): key being used. -1 defaults to self.key
            scale(str): scale being used. "" defaults to self.scale
            extended(bool): whether seventh chords will be used. Defaults to false.
        Returns:
            list(tuple(int)): the final sequence
        """
        # All input into this function should be done by the program and not the user.
        # Sequence length must an integer be greater than 1.
        # If not using default, sequence key must be an integer 0-11.
        # If not using default, sequence scale must be one of the ones defined in database.
        # set up
        if seq_key == -1:
            seq_key = self.key
        if seq_scale == "":
            seq_scale = self.scale
        
        diatonic_chords = db.diatonic_chords[seq_scale]
        diatonic_7th_chords = db.diatonic_7th_chords[seq_scale]
        final_sequence = []

        # generate seq_length number of chords
        for x in range(seq_length):
            if x%2 == 0:
                numeral = random.choice([0,3,5]) # tonic
            else:
                numeral = random.choice([1,2,4,6]) # sub-dominant/dominant

            # if chord extensions are requested...
            if extended:
                # randomly choose if we will add the seventh to the chord
                seventh = random.choice([True,False])
                if seventh:
                    transposed_chord = [(x + seq_key)%12 for x in diatonic_7th_chords[numeral]]
                else:
                    transposed_chord = [(x + seq_key)%12 for x in diatonic_chords[numeral]]
            # otherwise just use triads
            else:
                transposed_chord = [(x + seq_key)%12 for x in diatonic_chords[numeral]]

            # append to our final sequence
            final_sequence.append(transposed_chord)
        
        # after the sequence is generated, make sure that there is at least one I or i chord.
        tonic = [(x + seq_key)%12 for x in (0, 4, 7)]
        tonic_7th = [(x + seq_key)%12 for x in (0, 4, 7)]
        if (tonic not in final_sequence) and (tonic_7th not in final_sequence):
            if extended:
                # randomly choose if we will add the seventh to the chord
                seventh = random.choice([True,False])
                if seventh:
                    transposed_chord = [(x + seq_key)%12 for x in (0, 4, 7)]
                else:
                    transposed_chord = [(x + seq_key)%12 for x in (0, 4, 7)]
            # otherwise just use triads
            else:
                transposed_chord = [(x + seq_key)%12 for x in (0, 4, 7)]
    
        return final_sequence


# this is for testing
if __name__ == "__main__":

    # TEST 1: Sequence length
    # Each of these should print sequences with 4, 2, and 7 chords, respectively.
    # All of them will be chords from C major and not include extensions.
    print('Test 1')
    print(generate_sequence(4, 0, 'major'))
    print(generate_sequence(2, 0, 'major'))
    print(generate_sequence(7, 0, 'major'))

    # TEST 2: Sequence key
    # Each of these should print chords from C, E, and F# major, respectively.
    # Every integer should be between 0 and 11.
    # All of them will include 4 chords and not include extensions.
    print('Test 2')
    print(generate_sequence(4, 0, 'major'))
    print(generate_sequence(4, 4, 'major'))
    print(generate_sequence(4, 6, 'major'))

    # TEST 3: Sequence scale
    # Each of these should print chords from C minor, harmonic minor, and mixolydian, respectively.
    # All of them will include 4 chords and not include extensions.
    print('Test 3')
    print(generate_sequence(4, 0, 'minor'))
    print(generate_sequence(4, 0, 'harmonic minor'))
    print(generate_sequence(4, 0, 'mixolydian'))

    # TEST 4: Extensions
    # This should print 10 chords and should include at least one seventh chord.
    print('Test 4')
    print(generate_sequence(10, 0, 'major', True))

    # TEST 5: Tonic
    # Additionally, all of the sequences above should have at least one tonic chord.