#
# @lc app=leetcode.cn id=42 lang=python3

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Solution1: 采用左右指针向中间夹逼的方法解答此题
        解题思路：设定左右指针 l, r
                  假定左右两边最高的柱子分别为l_max, r_max, 初始化都为0
                  每次循环需要找到左右两边最高的柱子
                  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    step1:      left=0                               right=11
    l_max = max(l_max=0, height[0])=0                r_max = max(r_max=0, height[11])=1
    height[0] = 0                                    height[11] = 1 
        height[0] < height[11]
            sum + l_max - height[0] = 0
            left-->

    step2:l_max = max(l_max=0, height[1])=0               r_max = max(r_max=0, height[11])=1
        height[1] = 0                                     height[11] = 1

                                                        height[1] >= height[11]
                                                        sum + r_max - height[11] = 0
                                                        <-- right
        '''
        sum_res = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]:
               sum_res += left_max - height[left]
               left += 1
            else:
               sum_res += right_max - height[right]
               right -= 1

        return sum_res
# @lc code=end