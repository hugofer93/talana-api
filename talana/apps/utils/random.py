from typing import List

from numpy.random import default_rng


def get_random_value_in_list(id_list: List[int]) -> int:
    """Get random value in ID list.

    Args:
        id_list (List[int]): ID list to choice value.

    Returns:
        int: Value in list (ID).
    """
    range_ = default_rng()
    index = range_.choice(id_list, 1, replace=True)[0]
    return index
