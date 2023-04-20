
from notes import Note, Interval, transpose 
from keys import Key, KeyType
import chords as c

class TestKey(Key):

    
    def relative_key(self):
        """ Returns the relative key. If a Key is Major it will have a relative 
            Minor key (and vice-versa). This can be easily found on a instrument
            by going up or down 3 semitones.   

        Args:
            None.

        Returns:
            A Key.        
        """
        if self.type == KeyType.Major:
            new_note = transpose(self.root, Interval.m3, direction='d')
            return Key(new_note, KeyType.Minor)

        else:
            new_note = transpose(self.root, Interval.m3, direction='u')
            return Key(new_note, KeyType.Major)

    def _calculate_accidentals_count(self):
        """ 
        
        Args:
            None.

        Returns:
            An integer.        
        """
        if self.root == Note.C:
            self.accidentals = 0

        sharps = [Note.G, Note.D, Note.A, Note.E, Note.B, Note.Gb]
        flats = [Note.F, Note.Bb, Note.Eb, Note.Ab, Note.Db, Note.B]


        if self.root in flats:
            self.accidentals = flats.index(Note.Eb) + 1




        l = 10



        # self.accidentals = 0
        # direction = "u"
        # k = Key(self.root, self.type)

        # if self.type == KeyType.Minor:
        #     # direction = "d"
        #     k = self.relative_key()


        # note = Note.C

        # for i in range(7+1):
        #     if note == k.root:
        #         self.accidentals = i
        #     note = transpose(note, Interval.P5, direction) 





        x = 10




v = TestKey(Note.F, KeyType.Minor)
v._calculate_accidentals_count()

"""
Going to the right of the circle goes up a 5th and to the left goes down a 5th.

In the circle of 5ths, the outside are Major keys, the inside is Minor keys. This
shows the relative connection between the keys.

This shows how many sharps and flats are in the key.
"""
def circle_of_fifths():
    """ The circle of 5ths moves clockwise """


    # Order of Sharps
    # F C G D A E B
    # Fast Cars Go Dangerously Around Every Bend
    # 
    # orderre of flats is the revrsed
    #  B E A D G C F

    l, note = [], Note.C

    for i in range(7+1):
        l.append([i, note])
        note = transpose(note, Interval.P5) 

    return l

def circle_of_fourths():
    l, note = [], Note.C

    for i in range(7+1):
        l.append([i, note])
        note = transpose(note, Interval.P5, direction='d') 

    return l


print("fifths")
for f in circle_of_fifths():
    key = TestKey(f[1], KeyType.Major)
    key._calculate_accidentals_count()
    print(f, key, '->', key.relative_key(), key.accidentals)

print("fourths")
for f in circle_of_fourths():
    key = TestKey(f[1], KeyType.Major)
    key._calculate_accidentals_count()
    print(f, key, '->', key.relative_key(), key.accidentals)




# l = [TestKey(Note.C, KeyType.Major), 
#      TestKey(Note.A, KeyType.Minor),
#      TestKey(Note.Bb, KeyType.Minor),
#      ]

# for key in l:
#     print(key, '->', key.relative_key())



