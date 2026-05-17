class Solution:
    def twoSum(self, nums, target):
        mp = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mp:
                return [mp[diff], i]
            mp[n] = i