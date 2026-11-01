"""# 3867. Sum of GCD of Formed Pairs
from math import gcd

class Solution:
    def sumOfGcdPairs(self, nums):
        n = len(nums)
        prefixGcd = []

        mx = 0

        # Step 1: Build prefixGcd
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))

        # Step 2: Sort the array
        prefixGcd.sort()

        # Step 3: Pair smallest with largest
        left = 0
        right = n - 1
        ans = 0

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans"""

# Two Sum Problem 
nums = [2,7,11,15]
target = 9 

for i = 0 to n-1:
    for j = i+1 to n-1:
        if nums[i] + nums[j] == target:
            return [i, j]

