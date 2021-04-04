#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict_num:
                return [dict_num[diff], i]
            dict_num[n] = i
        return
        
# @lc code=end