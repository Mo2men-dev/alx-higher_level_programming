
    >>> matrix_mul("Hello", [[1, 2]])
    Traceback (most recent call last):
    TypeError: m_a must be a list

    >>> matrix_mul(["Betty", "Holberton"], [[1, 2]])
    Traceback (most recent call last):
    TypeError: m_a must be a list of lists

    >>> matrix_mul([[1, 2]], ["Betty", "Holberton"])
    Traceback (most recent call last):
    TypeError: m_b must be a list of lists

    >>> matrix_mul([], [[9, 4]])
    Traceback (most recent call last):
    ValueError: m_a can't be empty

    >>> matrix_mul([[9, 4]], [[]])
    Traceback (most recent call last):
    ValueError: m_b can't be empty

    >>> matrix_mul([[1, 2], ["Hello", 9]], [[9, 4], [2, 5]])
    Traceback (most recent call last):
    TypeError: m_a should contain only integers or floats

    >>> matrix_mul([[9, 4], [2, 5]], [[1, 2], ["Hello", 9]])
    Traceback (most recent call last):
    TypeError: m_b should contain only integers or floats

    >>> matrix_mul([[9, 4], [2]], [[1, 2], [4, 9]])
    Traceback (most recent call last):
    TypeError: each row of m_a must should be of the same size

    >>> matrix_mul([[9, 4], [2, 7.0]], [[1], [4, 9]])
    Traceback (most recent call last):
    TypeError: each row of m_b must should be of the same size

    >>> matrix_mul([[9, 4, 4], [2, 8, 2]], [[1, 2], [4, 9]])
    Traceback (most recent call last):
    ValueError: m_a and m_b can't be multiplied

    >>> matrix_mul([[9, 4, 4], [2, 8, 2]])
    Traceback (most recent call last):
    TypeError: matrix_mul() missing 1 required positional argument: 'm_b'

    >>> matrix_mul()
    Traceback (most recent call last):
    TypeError: matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'
