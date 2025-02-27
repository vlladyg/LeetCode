class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        max_el = 0
        for i in range(n):
            if nums[i][i] > max_el and is_prime(nums[i][i]):
                max_el = nums[i][i]

            if nums[i][n - i - 1] > max_el and is_prime(nums[i][n - i - 1]):
                max_el = nums[i][n - i - 1]

        return max_el

import math

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True
