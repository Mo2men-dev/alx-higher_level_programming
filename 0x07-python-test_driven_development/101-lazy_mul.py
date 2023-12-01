#!/usr/bin/python3
"""Module to multiply two matrices using NumPy"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy"""
    return numpy.matmul(m_a, m_b)
