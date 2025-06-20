from music_theory.instrument import StringInstrument
from music_theory.notes import Note, transpose
from music_theory.intervals import Interval

STANDARD_BASS_TUNING_INTERVALS = [
    Interval.Unison, Interval.P4, Interval.P4, Interval.P4
] 

STANDARD_GUITAR_TUNING_INTERVALS = [
    Interval.Unison, Interval.P4, Interval.P4, Interval.P4, Interval.M3, Interval.P4
] 

def create_standard_bass(note=Note.E):
    return StringInstrument.from_tuning_intervals(note, STANDARD_BASS_TUNING_INTERVALS)

def create_drop_bass(note=Note.D):
    bass = StringInstrument.from_tuning_intervals(transpose(note, Interval.M2, "up"), STANDARD_BASS_TUNING_INTERVALS)
    bass.tuning[0] = note
    return bass

def create_standard_guitar(note=Note.E):
    return StringInstrument.from_tuning_intervals(note, STANDARD_GUITAR_TUNING_INTERVALS)

def create_drop_guitar(note=Note.D):
    guitar = StringInstrument.from_tuning_intervals(transpose(note, Interval.M2, "up"), STANDARD_GUITAR_TUNING_INTERVALS)
    guitar.tuning[0] = note
    return guitar
    
def create_ukulele():
        return StringInstrument([Note.G, Note.C, Note.E, Note.A])

# Standard tunings
E_STANDARD_GUITAR = create_standard_guitar()
HALF_STEP_DOWN_GUITAR = create_standard_guitar(Note.Eb)
D_STANDARD_GUITAR = create_standard_guitar(Note.D)
C_STANDARD_GUITAR = create_standard_guitar(Note.C)

# Drop tunings
DROP_D_GUITAR = create_drop_guitar(Note.D)
DOUBLE_DROP_D_GUITAR = StringInstrument([Note.D, Note.A, Note.D, Note.G, Note.B, Note.D])
DROP_C_GUITAR = create_drop_guitar(Note.C)
DOUBLE_DROP_C_GUITAR = StringInstrument([Note.C, Note.G, Note.C, Note.F, Note.A, Note.D])

# Basses
E_STANDARD_BASS = create_standard_bass()
DROP_D_BASS = create_drop_bass(Note.D)

# Extended-range instruments
FIVE_STRING_BASS = StringInstrument([Note.B] + E_STANDARD_BASS.tuning)
SEVEN_STRING_GUITAR = StringInstrument([Note.B] + E_STANDARD_GUITAR.tuning)