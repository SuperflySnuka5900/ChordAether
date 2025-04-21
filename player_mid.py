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
<<<<<<< HEAD
        """ Here we are setting the instrument for the synthesizer 

        Arguments: program which is the MIDI program and bank which is
        the bank number to select from 

        """

        self.fs.program_select(0, self.sfid, bank, program)

    def get_driver(self):
        """ Here we are determining the audio driver

        Returns: the name of the audio driver for either Windows and 
        macOS/Linux 

        """

=======
        """Changes sound bank and program to match different instruments"""
        self.fs.program_select(0, self.sfid, bank, program)

    def get_driver(self):
        """Check for machine's os name and returns name of driver to make program compatible"""
>>>>>>> 790f6cdf622c82ae0a51e64324cea4d2708067e0
        if os.name == "nt":
            driver = "dsound"
        elif os.name == "posix":
            driver = "coreaudio"
        return driver
    
    def play_chords(self, chord_sequence, tempo=120):
        """ This is playing a senquence of chords

        Arguments: chord_sequence which is a list and tempo which
        is the tempo in beats per minute

        """

        delay = 60 / tempo
        for chord in chord_sequence:
            for note in chord:
                self.fs.noteon(0, note, 100)
            time.sleep(delay)
            for note in chord:
                self.fs.noteoff(0, note)

    def close(self):
        """ Here we shut down and delete the synthesizer instance 

        """

        self.fs.delete()
