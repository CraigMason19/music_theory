#-------------------------------------------------------------------------------
# Name:        mnemonics.py
#
# Notes:       A collection of mnemonics for musical concepts, reminders, 
#              tunings, and related topics.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import random

class Mnemonics:
    rhythm_spelling = "Rhythm Helps Your Two Hips Move"

    # Note rhythms
    note_length_animals = [
        { "length": "Quarter", "animal": "Dog" },
        { "length": "Eighths", "animal": "Chicken" },
        { "length": "Triplets", "animal": "Buffalo" },
        { "length": "Sixteenths", "animal": "Alligator" },
    ]

    # Notes on the stave
    treble_clef_lines = "Every Good Boy Deserves Football"
    treble_clef_spaces = "F A C E"
    bass_clef_lines = "Good Boys Deserve Football Always"
    bass_clef_spaces = "All Cows Eat Grass"

    # Tunings
    standard_guitar_tuning = [
        "Elephants And Donkeys Grow Big Ears",
        "Easter Bunnies Get Drunk At Easter",
        "Eddie Ate Dynamite Good Bye Eddie",
    ]

    standar_ukele_tuning = [
        "Goats Can Eat Anything"
    ]

    # Circle of 5ths 
    order_of_sharps = [
        "Father Charles Goes Down And Ends Battle",
        "Fast Cars Go Dangerously Around Every Bend",
        "Father Christmas Gave Dad An Electric Blanket",
    ]

    order_of_flats = [
        "Battle Ends And Down Goes Charles’s Father",
        "Before Eating A Doughnut Get Coffee First.",
        "Blanket Explodes And Dad Gets Cold Feet",
    ]

    order_of_sharps_flats_pairs = [
        {
            "sharps": "Father Charles Goes Down And Ends Battle",
            "flats":  "Battle Ends And Down Goes Charles’s Father"
        },
        {
            "sharps": "Father Christmas Gave Dad An Electric Blanket",
            "flats":  "Blanket Explodes And Dad Gets Cold Feet"
        },
    ]

    @staticmethod
    def random(option_list):
        return random.choice(option_list)