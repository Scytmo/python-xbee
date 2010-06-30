#! /usr/bin/python
"""
Fake.py

By Paul Malmsten, 2010
pmalmsten@gmail.com

Provides fake device objects for other unit tests.
"""

class FakeDevice:
    """
    Represents a fake serial port for testing purposes
    """
    def __init__(self):
        self.data = ''
    
    def write(self, data):
        """
        Writes data to the fake port for later evaluation
        """
        self.data = data
        
class FakeReadDevice:
    """
    Represents a fake serial port which can be read from in a similar
    fashion to the real thing
    """
    
    def __init__(self, data):
        self.data = data
        self.read_index = 0
        
    def read(self, length=1):
        """
        Read the indicated number of bytes from the port
        """
        # If too many bytes would be read, raise exception
        if self.read_index + length > len(self.data):
            raise ValueError("Not enough bytes exist!")
        
        read_data = self.data[self.read_index:self.read_index + length]
        self.read_index += length
        
        return read_data