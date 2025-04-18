#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 16:17:07 2025

@author: jamie
"""

import pygame.midi
import fluidsynth
import time
import os

class MidiPlayer:
    """Plays MIDI chords using FluidSynth for reliable cross-platform sound."""
    def __init__(self, soundfont_path="SM64SF V2.sf2"):
        if not os.path.exists(soundfont_path):
            raise FileNotFoundError(f"SoundFont not found: {soundfont_path}")
        
        self.fs = fluidsynth.Synth()
        self.fs.start(driver=self.get_driver())  # macOS; use "alsa" on Linux or "dsound" on Windows
        self.sfid = self.fs.sfload(soundfont_path)
        self.fs.program_select(0, self.sfid, 0, 0)

    def set_instrument(self, program, bank=0):
        self.fs.program_select(0, self.sfid, bank, program)

    def get_driver(self):
        if os.name == "nt":
            driver = "dsound"
        elif os.name == "posix":
            driver = "coreaudio"
        return driver
    
    def play_chords(self, chord_sequence, tempo=120):
        delay = 60 / tempo
        for chord in chord_sequence:
            for note in chord:
                self.fs.noteon(0, note, 100)
            time.sleep(delay)
            for note in chord:
                self.fs.noteoff(0, note)

    def close(self):
        self.fs.delete()
