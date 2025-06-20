import re

from music_theory.notes import Note, transpose, notes_to_string
from music_theory.intervals import Interval, interval_distance

def extract_frets(line):
    return [int(fret) for fret in re.findall(r"\d+", line)]

class StringInstrument:
    def __init__(self, tuning):
        if len(tuning) < 1:
            raise ValueError("Instruments must have at least 1 string")

        self.num_strings = len(tuning)
        self.tuning = tuning
        
    @classmethod 
    def from_tuning_intervals(cls, root_note, tuning_intervals):
        tuning = [root_note]  
        
        for interval in tuning_intervals[1:]: 
            tuning.append(transpose(tuning[-1], interval, "u"))

        return cls(tuning)   
        
    def add_capo(self, fret):
        if fret <= 0:
            raise ValueError("Capo must be placed on a positive fret")
        
        self.tuning = [transpose(n, Interval.from_index(fret), "u") for n in self.tuning]

    def adjust_string(self, string_index, interval, direction="u"):
        if string_index < 0 or string_index >= self.num_strings:
            raise ValueError(f"Incorrect string index {string_index}")
        
        self.tuning[string_index] = transpose(self.tuning[string_index], interval, direction)

    def detune(self, interval):
        self.tuning = [transpose(string, interval, direction="d") for string in self.tuning]
    
    def note_at_fret(self, string_index, fret):
        if string_index < 0 or string_index >= self.num_strings:
            raise ValueError(f"Incorrect string index {string_index}")

        if fret < 0:
            raise ValueError("Frets can't be negative")
        
        return Note.from_index(self.tuning[string_index].value + fret) 

    def notes_in_chord(self, chord_str):
        lines =  chord_str.split()

        if len(lines) != self.num_strings:
            raise ValueError(f"Expected {self.num_strings} strings, but got {len(lines)}")

        notes = []
        frets = extract_frets(chord_str)

        for string_index, string in enumerate(lines):
            frets = extract_frets(string)
            notes.extend([self.note_at_fret(string_index, fret) for fret in frets])

        return notes  

    def intervals_in_chord(self, chord_str):
        notes = self.notes_in_chord(chord_str)

        if len(notes) == 0:
            return []

        return [Interval.Unison] + [interval_distance(notes[0], notes[i+1]) for i in range(len(notes)-1)]

    def __str__(self):
        """ Returns a string representing the instrument. 

            e.g. str(StringInstrument([Note.B, Note.E, Note.A])) -> B, E, A, D, G

        Args:
            None.

        Returns:
            A string.
        """
        return f"{notes_to_string(self.tuning)}"

    def __repr__(self):
        """ Returns a string representing the instrument. 

            e.g. repr(StringInstrument([Note.B, Note.E, Note.A])) -> StringInstrument(3, [B, E, A])

        Args:
            None.

        Returns:
            A string.
        """
        return f"StringInstrument({self.num_strings}, [{notes_to_string(self.tuning)}])"