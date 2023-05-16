
# music_theory

A set of Python classes to help me learn music theory by implementing it.
 
 ### Features
- Transpose notes & calculate the interval distance.
- Builds scales of various lengths from various formulas (Interval, steps & numbers).
- Calculates all the modes of a note.
- Works out all the chords in a given key.
- Works out all the parallel chords in a given key.
- Works out all the dominant seventh chords in a given key.
- Can output the chords from a key from the roman numeral notation.  
  

## Requirements

No extra packages are needed.

## Examples

### Scales

To find all the modes of a note use the modes_from_note function inside scales.py

```python
for mode in modes_from_note(Note.C):
    print(mode)
```

```python
C Ionian: C, D, E, F, G, A, B
D Dorian: D, E, F, G, A, B, C
E Phrygian: E, F, G, A, B, C, D
F Lydian: F, G, A, B, C, D, E
G Mixolydian: G, A, B, C, D, E, F
A Aeolian: A, B, C, D, E, F, G
B Locrian: B, C, D, E, F, G, A
```

### Keys
To find a list of all chords in a key simply create a Key and use the pretty_print function. e.g.
```python
key = Key(Note.A, KeyType.Major)
key.pretty_print(dominant=True,  parallel=True)
```

```python
    AM        Bm       Dbm        DM        EM       Gbm     Abdim
     I        ii       iii        IV         V        vi       vii

    E7       Gb7       Ab7        A7        B7       Db7       Eb7
  V7/I     V7/ii    V7/iii     V7/IV      V7/V     V7/vi    V7/vii

    Am      Bdim        CM        Dm        Em        FM        GM
     i        ii       III        iv         v        VI       VII
```
