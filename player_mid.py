#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fluidsynth
import time
import os


class MidiPlayer:
    """Plays MIDI chords using FluidSynth for reliable cross-platform sound."""
    def __init__(self, soundfont_path="SM64SF V2.sf2"):
        """
        creates a FluidSynth instance and loads the specified SoundFont.
        Arguments: soundfont_path which is the path to the SoundFont file
        """
        if not os.path.exists(soundfont_path):
            raise FileNotFoundError(f"SoundFont not found: {soundfont_path}")
        
        self.fs = fluidsynth.Synth()
        self.fs.start(driver=self.get_driver())  # macOS; use "alsa" on Linux or "dsound" on Windows
        self.sfid = self.fs.sfload(soundfont_path)
        self.fs.program_select(0, self.sfid, 0, 0) # No banks, No presets

    def set_instrument(self, program, bank=0):
        """ Here we are setting the instrument for the synthesizer 

        Arguments: program which is the MIDI program and bank which is
        the bank number to select from 
        """
        self.fs.program_select(0, self.sfid, bank, program)

    def get_driver(self):
        """ Here we are determining the audio driver

        Returns: the name of the audio driver for either Windows and 
        macOS/Linux 
        NOTE: This is a simplified version and may not work on all systems.
        """

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
        """ 
        Here we shut down and delete the synthesizer instance 
        """
        self.fs.delete()
