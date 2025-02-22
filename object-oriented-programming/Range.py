class Range:
    """
    A class that mimic's the built-in range class.
    """

    def __init__(self, start, stop=None, step=1):
        """
        Initialize a range instance.

        Semantics is similar to built-in range class.
        """

        if step == 0:
            raise ValueError("Step cannot be 0")

        if stop is None:
            start, stop = 0, start

        # To also handle the case where start, stop is not divisible by step
        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index at k (using standard interpration if negative)."""
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError("Index out of range")

        # Indexing is 0 based
        return self._start + (k * self._step)
