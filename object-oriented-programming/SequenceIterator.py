class SequenceIterator:
    """An iterator of any of Python's sequence type"""

    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self._seq = sequence
        self._k = -1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1

        if self._k < len(self._seq):
            return self._seq[self._k]

        raise StopIteration()

    def __iter__(self):
        """By convention an iterator must return itself as an iterator"""
        return self
