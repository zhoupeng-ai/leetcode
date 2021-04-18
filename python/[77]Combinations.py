# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 563 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrace(i, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for j in range(i, n + 1):
                backtrace(j + 1, tmp + [j])

        backtrace(1, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
