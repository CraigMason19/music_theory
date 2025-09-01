"""
Defines the KeyType enumeration for musical keys, representing either major or minor.

This module provides:
- An Enum class `KeyType` with two values: Major and Minor.
- Utility methods to list all key types, select a random key type, and retrieve the parallel (opposite) key.
- String representations for clean display and debugging.

Example:
    from music_theory.key_type import KeyType

    kt = KeyType.Major
    print(f"Selected key: {kt}, Parallel: {kt.parallel}")
"""

import random
from enum import Enum

class KeyType(Enum):
    """ Represents a key type. Keys are either Major or Minor.
    
    Attributes:
        Type attributes:
            2 class attributes representing a Enum.

    Methods:
        items(cls):
            A class method to return the enums as a list.
        random(cls):
            A class method to return a random key type.
        parallel(self):
            A property that returns a parallel (opposite) key type.
        __str__(self):
            Returns the name of the key type.
        __repr__(self):
            Returns the Enum name.
    """
    (Major, Minor) = range(2) 

    @classmethod    
    def items(cls):
        """ A class method that returns a list of the key enumerations. 

            e.g. [KeyType.Major, KeyType.Minor ... ]

        Args:
            None.

        Returns:
            A list of key types.
        """  
        return [n for n in cls]

    @classmethod
    def random(cls):
        """ A class method that returns a random key type. 

            e.g. KeyType.Major

        Args:
            None.

        Returns:
            A KeyType.
        """  
        return random.choice(cls.items())

    @property
    def parallel(self):
        """ Returns the opposite KeyType. 

            e.g. C Minor is the parallel of C Major.

        Args:
            None.

        Returns:
            A KeyType
        """
        return KeyType.Minor if (self.name == 'Major') else KeyType.Major

    def __str__(self):
        """ Returns a string representing the key type name. 

            e.g. str(KeyType.Major) -> 'Major'

        Args:
            None.

        Returns:
            A string.
        """
        return self.name

    def __repr__(self):
        """ Returns a string representing the key types enum. 

            e.g. repr(KeyType.Major) -> 'KeyType.Major'

        Args:
            None.

        Returns:
            A string representing the key type's name.
        """
        return f'KeyType.{self.name}'