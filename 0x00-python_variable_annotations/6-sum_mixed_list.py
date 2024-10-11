#!/usr/bin/env python3
"""6-sum_mixed_list module"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Parameters
    ----------
    mxd_lst : list
        list of integers and floats

    Returns
    -------
    float
        the sum of the list
    """
    return sum(mxd_lst)
