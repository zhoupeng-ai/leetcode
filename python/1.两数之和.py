#
# @lc app=leetcode.cn id=1 lang=python3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Solution 1:暴力求解 O(N.pow(2))
        
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == target - nums[j]:
                    return [i, j]
        return []
        '''
        '''
        Solution 2:hash表O(N)
        '''
        hashmap = {}
        for idx, value in enumerate(nums):
            sub = target - value
            if sub in hashmap:
                return [hashmap[sub], idx]
            hashmap[value] = idx
        return None