import copy

from enum import Enum

from music_theory.notes import Note, Interval, transpose, notes_to_string

STANDARD_BASS_TUNING_INTERVALS = [
    Interval.Unison, Interval.P4, Interval.P4, Interval.P4
] 

STANDARD_GUITAR_TUNING_INTERVALS = [
    Interval.Unison, Interval.P4, Interval.P4, Interval.P4, Interval.M3, Interval.P4
] 

class String(Enum):
    (first, second, third, fourth, fifth, sixth) = range(6)

class TuningType:
    (standard, drop, open) = range(3)

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
        
    def with_capo(self, fret):
        new_instrument = copy.copy(self)
        new_instrument.tuning = [transpose(n, Interval.from_index(fret), "u") for n in self.tuning]

        return new_instrument

    def adjust_string(self, string_index, interval, direction="u"):
        try:            
            self.tuning[string_index] = transpose(self.tuning[string_index], interval, direction)
        except:
            raise ValueError(f"Incorrect string index {string_index}")

    def detune(self, interval):
        self.tuning = [transpose(string, interval, direction="d") for string in self.tuning]
    
    def note_at_fret(self, string_index, fret):
        if fret < -1:
            raise ValueError(f"Frets can't be negative")
        
        try:            
            return Note.from_index(self.tuning[string_index].value + fret)
        except:
            raise ValueError(f"Incorrect string index {string_index}")     

    def notes_at_frets(self, frets):
        if self.num_strings != len(frets):
            raise ValueError(f"All strings must be accounted for")
        
        #hmm
        
        # frets = [fret for fret in frets if fret not in {"x", "X", "-"}]

        # return [Note.from_index(self.tuning[string_index].value + fret)]

    def __str__(self):
        return f"{notes_to_string(self.tuning)}"

    def __repr__(self):
        return f"StringInstrument({self.num_strings}, [{notes_to_string(self.tuning)}])"


def create_bass(note=Note.E, tuning_type=TuningType.standard):
 
    match tuning_type:
        case TuningType.drop:
            guitar = StringInstrument.from_tuning_intervals(transpose(note, Interval.M2, "up"), STANDARD_BASS_TUNING_INTERVALS)
            guitar.adjust_string(0, Interval.M2, "down")
            return guitar

        case _:
            return StringInstrument.from_tuning_intervals(note, STANDARD_BASS_TUNING_INTERVALS)

def create_guitar(note=Note.E, tuning_type=TuningType.standard):
 
    match tuning_type:
        case TuningType.drop:
            guitar = StringInstrument.from_tuning_intervals(transpose(note, Interval.M2, "up"), STANDARD_GUITAR_TUNING_INTERVALS)
            guitar.adjust_string(0, Interval.M2, "down")
            return guitar

        case _:
            return StringInstrument.from_tuning_intervals(note, STANDARD_GUITAR_TUNING_INTERVALS)

def created_ukulele():
    return StringInstrument([Note.G, Note.C, Note.E, Note.A])

E_STANDARD_GUITAR = create_guitar()
HALF_STEP_DOWN_GUITAR = create_guitar(Note.Eb)
D_STANDARD_GUITAR = create_guitar(Note.D)
C_STANDARD_GUITAR = create_guitar(Note.C)

DROP_D_GUITAR = create_guitar(Note.D, TuningType.drop)
DROP_C_GUITAR = create_guitar(Note.C, TuningType.drop)
   
FIVE_STRING_BASS = StringInstrument([Note.B] + create_guitar().tuning)

UKELELE = created_ukulele()