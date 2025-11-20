from laba5 import *
import pytest
@pytest.fixture()
def get_prime_nums():
    prime_nums = []
    for num in range(1, 50):
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            prime_nums.append(num)
    return prime_nums

def test_fun_one(get_prime_nums):
    prime_nums = get_prime_nums
    assert fun_one(prime_nums) == [3, 4, 5, 7, 9, 13, 15, 19, 21, 25, 31, 33, 39, 43, 45, 49]

def test_fun_two(get_prime_nums):
    prime_nums = get_prime_nums
    assert fun_two(prime_nums) == [2, 4, 6, 10, 14, 22, 26, 34, 38, 46, 58, 62, 74, 82, 86, 94]

def test_fun_three(get_prime_nums):
    prime_nums = get_prime_nums
    assert fun_three(prime_nums) == [1, 4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209]

def test_three(get_prime_nums):
    prime_nums = get_prime_nums
    assert three(prime_nums) == [1, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]


def test_cube(get_prime_nums):
    prime_nums = get_prime_nums
    assert cube(prime_nums) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000, 9261]