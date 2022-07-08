#!/usr/bin/env python3

class String(str):
    """Extends the native string class to add new utility methods.\n
    Some of the added methods can change the value of the caller string,\n
    so these Strings are not always immutable like the native strings."""

    def __init__(self, aString):
        self.val = aString
    def __eq__(self, other):
        return str.__eq__(self.val, other)
    def __repr__(self):
        return str.__repr__(self.val)
    def __add__(self, other):
        return String(self.val + str(other))
    def __str__(self):
        return str.__str__(self.val)
    def __hash__(self):
        return str.__hash__(self.val)
    def __len__(self):
        return str.__len__(self.val)
    def __getitem__(self, i):
        return String(self.val.__getitem__(i))
    def __setitem__(self, i, v):
        self.val.__setitem__(i, v)
    def __int__(self):
        return int(self.val)
    def __float__(self):
        return float(self.val)
    @classmethod
    def fromdate(cls, date=None, format='%d/%m/%Y'):
        """ Instantiates a String from a date (datetime) and a format.\n
        In the absence of a date, the current date is used.\n
        An example of format: '%d/%m/%Y %H:%M:%S,%f' """
        import datetime
        if not date: date = datetime.datetime.today()  # Must be datetime, not time
        return cls(date.strftime(format))
    @staticmethod
    def strtodate(string, format='%d/%m/%Y'):
        import datetime
        return datetime.datetime.strptime(string, format)
    @staticmethod
    def concat(collection):
        """Function to turn a collection into a text."""
        output = String("")
        if isinstance(collection, list):
            output += "["
            for item in collection:
                if len(output) > 1:
                    output += ", "
                output += item
            output += "]"
        else:
            if isinstance(collection, dict):
                output += "{"
                for chave,value in collection.items():
                    if len(output) > 1:
                        output += ", "
                    output += chave + ": " + (value if type(value) not in [list, ] else String.concat(value))
                output += "}"
            else:
                from itertools import groupby
                if isinstance(collection, groupby):
                    output += "{"
                    for chave,value in collection:
                        if len(output) > 1:
                            output += ", "
                        output += chave + ": " + String.concat(list(value))
                    output += "}"
                else:
                    raise Exception("Unrecognized type for String concatenation: " + str(type(collection)))
        return output
    def todate(self, format='%d/%m/%Y'):
        return String.strtodate(self.val, format)
    def since(self, start):
        return String(self.partition(start)[2])
    def until(self, end):
        return String(self.partition(end)[0])
    def since_including(self, start):
        part = self.partition(start)
        return String(part[1]+part[2])
    def until_including(self, end):
        part = self.partition(end)
        return String(part[0]+part[1])
    def since_last(self, start, including_start=False):
        part = self.rpartition(start)
        return String(part[1]+part[2]) if including_start else String(part[2]) 
    def until_last(self, end, including_end=False):
        part = self.rpartition(end)
        return String(part[0]+part[1]) if including_end else String(part[0]) 
    def contains_all(self, *strings):
        return all(x in self for x in strings)
    def int(self):
        return int(self)
    def strip(self):
        return String(str.strip(self))
    def trim(self):
        """ Mutable version of strip() """
        self.val = str.strip(self)
        return self
    def replace(self, old, new):
        return String(str.replace(self, old, new))
    def change(self, old, new):
        """ Mutable version of replace() """
        self.val = str.replace(self, old, new)
        return self
    def remove_last(self, n):
        return String(self[0 : len(self) - n])
    def cut(self, *separator):
        return [String(s) for s in str.split(self, *separator)]
    def lines(self):
        return [String(l) for l in self.val.splitlines() if l and l.strip()]
    def lines_with(self, *strings):
        return [l for l in self.cut('\n') if all(s in l for s in strings)]
    def line_with(self, *strings):
        lines = self.lines_with(*strings)
        assert(len(lines) <= 1)
        return lines[0] if lines else None
    def cells_with(self, *strings):
        return [c for c in self.cut() if all(s in c for s in strings)]
    def cell_with(self, *strings):
        cells = self.cells_with(*strings)
        assert(len(cells) <= 1)
        return cells[0] if cells else None
    def empty(self):
        return not self.val or not self.val.strip()
    def add(self, s, index=None):
        """ Mutable method. Concatenates string in specific position. """
        if index:
            self.val = self.val[:index] + s + self.val[index:]
        else: self.val += s
        return self
    def mask(self, format):
        """ Mutable method. Applies a mask to the String.\n 
        Each character from the String replaces (in order) each symbol (#) from the mask. \n 
        The extra characters are inserted when/if needed. """
        assert len(format) >= len(self.val) and format.count('#') <= len(self.val)
        mask_chars = {}
        for index, c in enumerate(format):
            if c != '#':
                mask_chars[index] = c
        for index, c in mask_chars.items():
            if self[index] != c:
                self.add(c, index)
        return self
