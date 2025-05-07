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

        #Creates MIDI messages for each note in the chord sequence and adds them to the track
        for chord_notes in chord_sequence:
            for note in chord_notes:
                track.append(Message('note_on', note=note, velocity=64, time=0))
            for note in chord_notes:
                track.append(Message('note_off', note=note, velocity=64, time=480 if note == chord_notes[0] else 0))

        mid.save(filename)
        """Prints file name"""
        print(f"Saved MIDI file: {filename}")

# This is for testing
if __name__ == "__main__":
    testWriter = MidiWriter()
    test_sequence = [(60, 64, 67), (62, 65, 69), (64, 67, 71)]
    testWriter.save_midi(test_sequence)
    # Go to https://pianotify.com/import-midi-file and upload the midi file that was just created.
    # It should produce a CM, Dm, and Em chord in a row.