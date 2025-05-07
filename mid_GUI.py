#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is part of ChordAscend, a MIDI chord progression generator and player.
It provides a GUI for users to interact with the chord generation and playback features.
"""

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, 
    QHBoxLayout, QComboBox, QSlider, QFileDialog
)
import sys
from mid_writer import MidiWriter
from player_mid import MidiPlayer

class ChordApp(QWidget):
    """
    Main application class for the ChordAscend GUI.
    This class handles the user interface and interactions for generating and playing MIDI chord progressions.
    """
    def __init__(self):
        """
        Initialize the ChordApp.
        Sets up the main window, layout, and UI components.
        """
        super().__init__()
        self.setWindowTitle("ChordAscend")
        self.setGeometry(100, 100, 400, 350)
        self.init_ui()
        #we need to connect the logic from the engine to here
        # Placeholder for chord sequence
        self.chord_sequence = [[60, 64, 67], [62, 65, 69], [64, 67, 71]]  # Mock chords: C, Dm, Em
        self.player = MidiPlayer()

    def init_ui(self):
        """
        Initialize the user interface components.
        Sets up the layout, buttons, labels, and other widgets.
        """
        layout = QVBoxLayout()

        # Chord Display
        self.chord_label = QLabel("I – IV – V – vi")
        layout.addWidget(self.chord_label)

        # Playback + Controls
        controls_layout = QHBoxLayout()
        self.play_btn = QPushButton("Play")
        self.regen_btn = QPushButton("Regenerate")
        self.export_btn = QPushButton("Export MIDI")
        controls_layout.addWidget(self.play_btn)
        controls_layout.addWidget(self.regen_btn)
        controls_layout.addWidget(self.export_btn)
        layout.addLayout(controls_layout)

        # Settings
        settings_layout = QHBoxLayout()
        self.key_selector = QComboBox()
        self.key_selector.addItems(["C","C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A","A#/Bb", "B"])
        settings_layout.addWidget(QLabel("Key:"))
        settings_layout.addWidget(self.key_selector)

        # BPM Slider
        self.bpm_slider = QSlider()
        self.bpm_slider.setOrientation(1)  # Horizontal
        self.bpm_slider.setMinimum(40)
        self.bpm_slider.setMaximum(250)
        self.bpm_slider.setSingleStep(1)
        self.bpm_slider.setValue(120)
        
        # BPM Label
        self.bpm_label = QLabel("BPM: 120")
        
        # Connect slider movement to label update
        self.bpm_slider.valueChanged.connect(
        lambda value: self.bpm_label.setText(f"BPM: {value}")
        )
        # Connect buttons to functions
        #self.regen_btn.clicked.connect(self.regenerate_chord_progression)
        self.play_btn.clicked.connect(self.play_progression)
        self.export_btn.clicked.connect(self.export_midi)
        self.regen_btn.clicked.connect(self.regenerate_chord_progression)

        # Add widgets to layout
        settings_layout.addWidget(self.bpm_label)
        settings_layout.addWidget(self.bpm_slider)
        
         # Instrument dropdown
         # instrements are from the SM64SF.sf2 file
        self.instrument_selector = QComboBox()
        self.instrument_selector.addItems([
            "0 - Grand Piano",
            "4 - Bells",
            "6 - Harpsichord",
            "24 - Nylon Guitar",
            "40 - Violin",
            "56 - Trumpet",
            "68 - Synth Brass",
            "73 - Flute",
            "82 - VOX",
            "118 - Synth Drum",
        ])
        layout2 = QHBoxLayout()
        layout2.addWidget(QLabel("Instrument:"))
        layout2.addWidget(self.instrument_selector)
        self.instrument_selector.currentIndexChanged.connect(self.change_instrument)

        # Add all layouts to main layout
        layout.addLayout(settings_layout)
        layout.addLayout(layout2)
        self.setLayout(layout)

    def play_progression(self):
        """
        Play the current chord progression using the selected tempo.
        calls the MidiPlayer to play the chords.
        See: player_mid.py for the MidiPlayer class.
        """
        tempo = self.bpm_slider.value()
        self.player.play_chords(self.chord_sequence, tempo=tempo)

    def export_midi(self):
        """
        Export the current chord progression to a MIDI file.
        Opens a file dialog for the user to select the save location.
        calls the MidiWriter to save the file.
        See: midi_writer.py for the MidiWriter class.
        """
        filename, _ = QFileDialog.getSaveFileName(self, "Save MIDI File", "", "MIDI files (*.mid)")
        if filename:
            MidiWriter.save_midi(self.chord_sequence, filename)
   
    def change_instrument(self):
        """
        Change the instrument based on the selected item in the dropdown.
        Updates the MidiPlayer's instrument selection.
        See: line 89 for the instrument mapping.
        """
        selected_text = self.instrument_selector.currentText()
        program_number = int(selected_text.split(" - ")[0])
        self.player.set_instrument(program_number)

    def regenerate_chord_progression(self):
        # Placeholder for regeneration logic
        #step 1: Get the selected key number
        #Step 2: randomly choose a scale OR add a scale selector // pass major, minor
        #step 3: choose either a place holder length and extend bool // length be 4 bool = false
        #step 4: call the chord logic to generate a sequence
        pass
    def get_selected_key_number(self):
        """
        Get the selected key number based on the key selector dropdown.
        Maps the selected key to a number (0-11) representing the MIDI note number.
        """
        key_text = self.key_selector.currentText()
        key_mapping = {
            "C": 0,
            "C#/Db": 1,
            "D": 2,
            "D#/Eb": 3,
            "E": 4,
            "F": 5,
            "F#/Gb": 6,
            "G": 7,
            "G#/Ab": 8,
            "A": 9,
            "A#/Bb": 10,
            "B": 11
        }
        return key_mapping.get(key_text, 0)  # Default to C if not found




# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChordApp()
    window.show()
    sys.exit(app.exec_())

# Testing
    # Running this program should cause a window to pop up with several
    # interactive buttons and dropdown boxes. Each of the interactive
    # elements should do as written in the comments for that element.