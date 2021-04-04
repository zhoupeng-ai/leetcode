#
# @lc app=leetcode.cn id=66 lang=python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        Solution 1: 将数组转换成为整数，加1之后再拆成数组
        
        stri = "".join([str(i) for i in digits])
        resi = int(stri) + 1
        return [int(i) for i in str(resi)]
        '''
        '''
        Solution 2: 从数组的最后一位开始+1, 并对10取余，如果余数不为0（不需要进位），则直接返回数组
                    需要进位是继续向下循环，
                    如果原数组全部为0，则需要在数组索引为0的位置插入1
        '''
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0 :
                return digits  
        digits.insert(0, 1)  # 在数组的位置0添加1
        return digits
