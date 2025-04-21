#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fluidsynth
import time
import os

class MidiPlayer:
    """Plays MIDI chords using FluidSynth for reliable cross-platform sound."""
    def __init__(self, soundfont_path="SM64SF V2.sf2"):
        """Initializes the midi player with a sound font and connects it to the driver"""
        if not os.path.exists(soundfont_path):
            raise FileNotFoundError(f"SoundFont not found: {soundfont_path}")
        """Raises error if file is not found"""
        self.fs = fluidsynth.Synth()
        """Creates a synth object in fluidsynth that generates a synthesizer object to control sound generation"""
        self.fs.start(driver=self.get_driver())  # macOS; use "alsa" on Linux or "dsound" on Windows
        """Refers to the get_driver function to connect the synthesizer to the driver"""
        self.sfid = self.fs.sfload(soundfont_path)
        """Loads the sound font into the synthesizer"""
        self.fs.program_select(0, self.sfid, 0, 0)
        """Checks for channel, sound font id, bank, and the preset"""

    def set_instrument(self, program, bank=0):
        """Changes sound bank and program to match different instruments"""
        self.fs.program_select(0, self.sfid, bank, program)

    def get_driver(self):
        """Check for machine's os name and returns name of driver to make program compatible"""
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
