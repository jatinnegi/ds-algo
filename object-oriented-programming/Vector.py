class Vector:
    """Represent a vector in multidimensional space."""

    def __init__(self, d):
        """Create a d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth co-ordinate of the vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth item of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")

        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other

    def __str__(self):
        return f"<{str(self._coords)[1:-1]}>"
