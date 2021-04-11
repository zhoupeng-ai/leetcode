#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        _map = {}
        for i in strs:
            sort_i = ''.join(sorted(i))
            if sort_i in _map:
                ret[_map[sort_i]].append(i)
            else:
                _map[sort_i] = len(ret)
                ret.append([i])
        return ret

# @lc code=end

