

import pytest
from sorting import (
    quick_sort,
    bubble_sort,
    heap_sort,
    merge_sort,
    insertion_sort
)


test_data = [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [5, 2, 3, 1, 4],
    [10, -1, 3, 0, 7, 7, 2],
    list(range(10, 0, -1)),  
]


@pytest.mark.parametrize("arr", test_data)
def test_quick_sort(arr):
    assert quick_sort(arr) == sorted(arr)


@pytest.mark.parametrize("arr", test_data)
def test_bubble_sort(arr):
    assert bubble_sort(arr) == sorted(arr)


@pytest.mark.parametrize("arr", test_data)
def test_heap_sort(arr):
    assert heap_sort(arr) == sorted(arr)


@pytest.mark.parametrize("arr", test_data)
def test_merge_sort(arr):
    assert merge_sort(arr) == sorted(arr)


@pytest.mark.parametrize("arr", test_data)
def test_insertion_sort(arr):
    assert insertion_sort(arr) == sorted(arr)