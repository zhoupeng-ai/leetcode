#
# @lc app=leetcode.cn id=21 lang=python3
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        _head = ListNode()
        tmp = _head
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = l2
                tmp = tmp.next
                l2 = l2.next
        
        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2

        return _head.next