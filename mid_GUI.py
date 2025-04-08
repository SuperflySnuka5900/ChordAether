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

class ChordApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChordAscend")
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()

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
        self.key_selector.addItems(["C", "D", "E", "F", "G", "A", "B"])
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
        
        # Add widgets to layout
        settings_layout.addWidget(self.bpm_label)
        settings_layout.addWidget(self.bpm_slider)
        
        layout.addLayout(settings_layout)
        self.setLayout(layout)



# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChordApp()
    window.show()
    sys.exit(app.exec_())
