#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 21:28:20 2025

@author: jamie
"""

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, 
    QHBoxLayout, QComboBox, QSlider, QFileDialog
)
import sys
from mid_writer import MidiWriter
from player_mid import MidiPlayer

class ChordApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChordAscend")
        self.setGeometry(100, 100, 400, 350)
        self.init_ui()
        self.chord_sequence = [[60, 64, 67], [62, 65, 69], [64, 67, 71]]  # Mock chords: C, Dm, Em
        self.player = MidiPlayer()

    def init_ui(self):
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

        # Add widgets to layout
        settings_layout.addWidget(self.bpm_label)
        settings_layout.addWidget(self.bpm_slider)
        
         # Instrument dropdown
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

        layout.addLayout(settings_layout)
        layout.addLayout(layout2)
        self.setLayout(layout)

    def play_progression(self):
        tempo = self.bpm_slider.value()
        self.player.play_chords(self.chord_sequence, tempo=tempo)

    def export_midi(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save MIDI File", "", "MIDI files (*.mid)")
        if filename:
            MidiWriter.save_midi(self.chord_sequence, filename)
   
    def change_instrument(self):
        selected_text = self.instrument_selector.currentText()
        program_number = int(selected_text.split(" - ")[0])
        self.player.set_instrument(program_number)

    def regenerate_chord_progression(self):
        # Placeholder for regeneration logic
        # self.chord_sequence = generate_new_chord_sequence()
        # self.chord_label.setText("New Chord Sequence")
        pass




# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChordApp()
    window.show()
    sys.exit(app.exec_())
