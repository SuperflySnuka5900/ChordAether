#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 16:17:07 2025

@author: jamie
"""

from mido import Message, MidiFile, MidiTrack

class MidiWriter:
    """Handles creating and saving MIDI files from chord progressions."""
    
    @staticmethod
    def save_midi(chord_sequence, filename="chord_progression.mid"):
        """Saves the chord progression as a MIDI file."""
        mid = MidiFile() 
        track = MidiTrack()
        mid.tracks.append(track)

        for chord_notes in chord_sequence:
            """Separates the chords and orders them."""
            for note in chord_notes:
                """Creates the chords with notes."""
                track.append(Message('note_on', note=note, velocity=64, time=0))
            """Separates chords from each other."""
            track.append(Message('note_off', note=note, velocity=64, time=480))

        mid.save(filename)
        """Prints file name"""
        print(f"Saved MIDI file: {filename}")
