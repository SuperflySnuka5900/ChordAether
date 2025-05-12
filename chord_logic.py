#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file provides chord logic to ordering chords into a progression.
"""

import database as db
import random

class Sequence():
    """This class is used for creating a sequence and keeping information about it.
    Attributes:
        key(int): Key in integer form
        scale(str): Name of the scale being used
        numerals(list(str)): Numerals for the chord sequence
        pitches(list(tuple(int))): Tuples representing chords using integer pitches
    """

    def __init__(self, key, scale, seq_length, extended = False):
        """Generate a sequence and populate its attributes upon creation.
        Args:
            key(int): Key in integer form
            scale(str): Name of the scale being used
            seq_length(int): Number of chords to be generated
            extended(bool): Whether or not to use seventh chords
        """
        self.key = key
        self.scale = scale
        self.generate_sequence(seq_length, extended)


    def generate_sequence(self, seq_length, extended = False):
        """Generates a sequence using the given parameters.
        Args:
            seq_length(int): length of the sequence
            extended(bool): whether seventh chords will be used. Defaults to false.
        Side Effects:
            Creates numerals and pitches attributes and populates their lists.
        """
        # All input into this function should be done by the program and not the user.
        # Sequence length must an integer be greater than 1.
        
        # set up
        seq_key = self.key
        seq_scale = self.scale
        
        diatonic_chords = db.diatonic_chords[seq_scale]
        diatonic_7th_chords = db.diatonic_7th_chords[seq_scale]
        
        self.numerals = []
        self.pitches = []

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

            # append to our sequence attributes
            self.pitches.append(transposed_chord)

            if len(transposed_chord) == 3: # triad
                self.numerals.append(db.diatonic_triad_numerals[seq_scale][numeral])
            else:
                self.numerals.append(db.diatonic_7th_numerals[seq_scale][numeral])
        
        # after the sequence is generated, make sure that there is at least one I or i chord.
        tonic = db.diatonic_triad_numerals[seq_scale][0]
        tonic_7th = db.diatonic_7th_numerals[seq_scale][0]

        if (tonic not in self.numerals) and (tonic_7th not in self.numerals):
            # determine chord notes
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
            
            # edit the existing sequence
            self.pitches[0] = transposed_chord

            if len(transposed_chord) == 3: # triad
                self.numerals[0] = db.diatonic_triad_numerals[seq_scale][0]
            else:
                self.numerals[0] = db.diatonic_7th_numerals[seq_scale][0]
        

    def get_label(self):
        """Generate a string of the numerals in the sequence.
        Returns:
            str: nicely formatted string of the sequence's Roman numerals
        """
        final_str = self.numerals[0]
        for i in range(1, len(self.numerals)):
            final_str += f" – {self.numerals[i]}"
        return final_str


# this is for testing
if __name__ == "__main__":

    mySeq = Sequence(0,'major')

    # TEST 1: Sequence length
    # Each of these should print sequences with 4, 2, and 7 chords, respectively.
    # All of them will be chords from C major and not include extensions.
    print('Test 1')
    print(mySeq.generate_sequence(4, 0, 'major'))
    print(mySeq.generate_sequence(2, 0, 'major'))
    print(mySeq.generate_sequence(7, 0, 'major'))

    # TEST 2: Sequence key
    # Each of these should print chords from C, E, and F# major, respectively.
    # Every integer should be between 0 and 11.
    # All of them will include 4 chords and not include extensions.
    print('Test 2')
    print(mySeq.generate_sequence(4, 0, 'major'))
    print(mySeq.generate_sequence(4, 4, 'major'))
    print(mySeq.generate_sequence(4, 6, 'major'))

    # TEST 3: Sequence scale
    # Each of these should print chords from C minor, harmonic minor, and mixolydian, respectively.
    # All of them will include 4 chords and not include extensions.
    print('Test 3')
    print(mySeq.generate_sequence(4, 0, 'minor'))
    print(mySeq.generate_sequence(4, 0, 'harmonic minor'))
    print(mySeq.generate_sequence(4, 0, 'mixolydian'))

    # TEST 4: Extensions
    # This should print 10 chords and should include at least one seventh chord.
    print('Test 4')
    print(mySeq.generate_sequence(10, 0, 'major', True))

    # TEST 5: Tonic
    # Additionally, all of the sequences above should have at least one tonic chord.