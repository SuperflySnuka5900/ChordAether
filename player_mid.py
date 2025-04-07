#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 16:17:07 2025

@author: jamie
"""

import pygame.midi
import time

class MidiPlayer:
    """Handles MIDI playback using pygame."""
    
    def __init__(self):
        pygame.midi.init()
        self.device_id = pygame.midi.get_default_output_id()
        self.midi_out = pygame.midi.Output(self.device_id)

    def play_chords(self, chord_sequence, tempo=120):
        """Plays the chord progression at the given tempo."""
        delay = 60 / tempo  # Convert BPM to seconds per beat

        for chord in chord_sequence:
            for note in chord:
                self.midi_out.note_on(note, velocity=64)
            time.sleep(delay)  # Hold chord
            for note in chord:
                self.midi_out.note_off(note, velocity=64)

    def close(self):
        """Closes the MIDI player."""
        self.midi_out.close()
        pygame.midi.quit()