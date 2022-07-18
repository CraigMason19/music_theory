#-------------------------------------------------------------------------------
# Name:        caller.py
#
# Notes:       A caller that shows the usage of the music classes.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from notes import Note
from scales import Scale, ScaleType

def main():
    s = Scale(Note.C, ScaleType.Dorian)

    print(s)
    print(str(s))
    print(repr(s))

if __name__ == '__main__':
    main()