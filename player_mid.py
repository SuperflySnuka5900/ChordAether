#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 16:17:07 2025

@author: jamie
"""

import pygame.midi
import time

class MidiPlayer:
    def __init__(self):
        pygame.midi.init()
        self.device_id = pygame.midi.get_default_output_id()
        if self.device_id == -1:
            print("⚠️ No MIDI output device found.")
            self.midi_out = None
        else:
            self.midi_out = pygame.midi.Output(self.device_id)

    def play_chords(self, chord_sequence, tempo=120):
        if not self.midi_out:
            print("❌ Cannot play MIDI: No output device.")
            return
        delay = 60 / tempo
        for chord in chord_sequence:
            for note in chord:
                self.midi_out.note_on(note, velocity=64)
            time.sleep(delay)
            for note in chord:
                self.midi_out.note_off(note, velocity=64)

    def close(self):
        if self.midi_out:
            self.midi_out.close()
        pygame.midi.quit()