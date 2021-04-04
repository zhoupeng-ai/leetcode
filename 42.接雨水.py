#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (54.28%)
# Likes:    2223
# Dislikes: 0
# Total Accepted:    223.7K
# Total Submissions: 405.4K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 
# 
# 示例 2：
# 
# 
# 输入：height = [4,2,0,3,2,5]
# 输出：9
# 
# 
# 
# 
# 提示：
# 
# 
# n == height.length
# 0 
# 0 
# 
# 
#

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