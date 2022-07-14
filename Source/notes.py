#-------------------------------------------------------------------------------
# Name:        music_notes.py
#
# Notes:       A representation of the 12 notes of the musical scale
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from enum import Enum

class Note(Enum):
    C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B = range(12) 

class Interval(Enum):
    Unison, m2, M2, m3, M3, P4, dim5, P5, m6, M6, m7, M7 = range(12) 

def notes_to_string(note_list):
    return ', '.join([n.name for n in note_list])

def intervals_to_string(interval_list):
    return ', '.join([i.name for i in interval_list])

def interval_distance(root, interval):
    pass

def note_above(note, step='h'):
    pass
    
def note_below(note, step='h'):
    pass
    
def main():
    n = Note.C
    ns = notes_to_string([Note.C, Note.B, Note.D])

    print(n)
    print(ns)


 

if __name__ == '__main__':
    main()