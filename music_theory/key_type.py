"""
Defines the KeyType enumeration for musical keys, representing either major or 
minor.

This module provides:
- An Enum class `KeyType` with two values: Major and Minor.
- Utility methods to list all key types, select a random key type, and retrieve
  the parallel (opposite) key.
- String representations for clean display and debugging.

Example:
    >>> from music_theory.key_type import KeyType
    >>> kt = KeyType.Major
    >>> print(f"Selected key: {kt}, Parallel: {kt.parallel}")
    Selected key: Major, Parallel: Minor
"""

import random

from enum import Enum
from typing import Self

class KeyType(Enum):
    """ 
    Represents a key type. Keys are either Major or Minor.
    
    Attributes:
        Type attributes:
            2 class attributes representing a Enum.

    Methods:
        items(cls):
            A class method to return the enums as a list.
        all(cls):
            An alias for items(), returning the enums as a list.
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
    def items(cls) -> list[Self]:
        """ 
        A class method that returns a list of the key enumerations. 

        Example:
            >>> KeyType.items()
            [KeyType.Major, KeyType.Minor]

        Returns:
            list[KeyType]:
        """  
        return [n for n in cls]

    all = items  # Alias
    
    @classmethod
    def random(cls) -> Self:
        """
        A class method that returns a random key type. 

        Returns:
            KeyType:
        """  
        return random.choice(cls.items())

    @property
    def parallel(self) -> Self:
        """ 
        Returns the opposite KeyType. 

        Example:
            >>> KeyType.Major.parallel
            KeyType.Minor

        Returns:
            KeyType:
        """
        return KeyType.Minor if (self.name == 'Major') else KeyType.Major

    def __str__(self) -> str:
        """ 
        Returns a string representing the key types enum name. 

        Example:
            >>> str(KeyType.Major)
            Major
        
        Returns:
            str:
        """
        return self.name

    def __repr__(self) -> str:
        """ 
        Returns a string representing the key types class and enum name. 

        Example:
            >>> repr(KeyType.Major)
            KeyType.Major

        Returns:
            str:
        """
        return f'KeyType.{self.name}'