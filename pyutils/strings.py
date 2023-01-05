from __future__ import annotations # This might be unnecessary in the future.


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
    def fromdate(cls, date=None, format='%d/%m/%Y') -> String:
        """ Instantiates a String from a date (datetime) and a format.\n
        In the absence of a date, the current date is used.\n
        An example of format: '%d/%m/%Y %H:%M:%S,%f' """
        import datetime
        if not date: date = datetime.datetime.today()  # Must be datetime, not time
        return cls(date.strftime(format))
    @staticmethod
    def strtodate(string: str, format='%d/%m/%Y'):
        import datetime
        return datetime.datetime.strptime(string, format)
    @staticmethod
    def concat(collection) -> String:
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
    def startingwith(self, start: str, occurrence=1) -> String:
        """Returns the substring starting at (and including) the given text until the end.\n
        The optional 'ocurrence' parameter can be used to consider the Nth ocurrence of the text.\n
        An IndexError is raised it the text is not found.\n
        For occurrence=1 (default), consider using the native start+str.partition(start)[2].\n
        For last occurrence, consider using the native start+str.rpartition(start)[2].
        """
        return String(start + self.split(start, occurrence)[occurrence])
    def startingafter(self, start: str, occurrence=1) -> String:
        """Returns the substring starting at (NOT including) the given text until the end.\n
        The optional 'ocurrence' parameter can be used to consider the Nth ocurrence of the text.\n
        An IndexError is raised it the text is not found.\n
        For occurrence=1 (default), consider using the native str.partition(start)[2].\n
        For last occurrence, consider using the native str.rpartition(start)[2]."""
        return String(self.split(start, occurrence)[occurrence])
    def endingwith(self, end: str, occurrence=1) -> String:
        """Returns the substring from the beginning until (and including) the given text.\n
        The optional 'ocurrence' parameter can be used to consider the Nth ocurrence of the text.\n
        An IndexError is raised it the text is not found.\n
        For occurrence=1 (default), consider using the native str.partition(end)[0]+end.\n
        For last occurrence, consider using the native str.rpartition(end)[0]+end.\n
        For a known Nth ocurrence (but not first or last), consider using the native str.rsplit(end, ocurrence)[0]+end."""
        return String(end.join(self.split(end, occurrence)[:occurrence]) + end)
    def endingbefore(self, end: str, occurrence=1) -> String:
        """Returns the substring from the beginning until (NOT including) the given text.\n
        The optional 'ocurrence' parameter can be used to consider the Nth ocurrence of the text.\n
        An IndexError is raised it the text is not found.\n
        For occurrence=1 (default), consider using the native str.partition(end)[0].\n
        For last occurrence, consider using the native str.rpartition(end)[0].\n
        For a known Nth ocurrence (but not first or last), consider using the native str.rsplit(end, ocurrence)[0]."""
        return String(end.join(self.split(end, occurrence)[:occurrence]))
    def contains_all(self, *strings: str) -> bool:
        return all(x in self for x in strings)
    def contains_any(self, *strings: str) -> bool:
        return any(x in self for x in strings)
    def int(self) -> int:
        return int(self)
    def strip(self) -> String:
        return String(str.strip(self))
    def trim(self) -> String:
        """ Mutable version of strip() """
        self.val = str.strip(self)
        return self
    def replace(self, old: str, new: str) -> String:
        return String(str.replace(self, old, new))
    def change(self, old: str, new: str) -> String:
        """ Mutable version of replace() """
        self.val = str.replace(self, old, new)
        return self
    def remove_last(self, n: int) -> String:
        return String(self[0 : len(self) - n])
    def cut(self, *separator: str):
        return [String(s) for s in str.split(self, *separator)]
    def lines(self):
        return [String(l) for l in self.val.splitlines() if l and l.strip()]
    def lines_with(self, *strings: str):
        return [l for l in self.cut('\n') if all(s in l for s in strings)]
    def line_with(self, *strings: str) -> String:
        lines = self.lines_with(*strings)
        assert(len(lines) <= 1)
        return lines[0] if lines else None
    def cells_with(self, *strings: str):
        return [c for c in self.cut() if all(s in c for s in strings)]
    def cell_with(self, *strings: str) -> String:
        cells = self.cells_with(*strings)
        assert(len(cells) <= 1)
        return cells[0] if cells else None
    def empty(self) -> bool:
        return not self.val or not self.val.strip()
    def add(self, string: str, index=None) -> String:
        """ Mutable method. Concatenates string in specific position. """
        if index:
            self.val = self.val[:index] + string + self.val[index:]
        else: self.val += string
        return self
    def mask(self, format: str) -> String:
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
