#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (57.60%)
# Likes:    7468
# Dislikes: 905
# Total Accepted:    693.2K
# Total Submissions: 1.2M
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [2,1], x = 2
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy_smaller = ListNode(-201)
        smaller = dummy_smaller

        dummy_bigger = ListNode(201)
        bigger = dummy_bigger

        curr = head

        while curr:
            if curr.val < x:
                smaller.next = curr
                smaller = smaller.next
            else:
                bigger.next = curr
                bigger = bigger.next
            curr = curr.next

        # **这里是改进的地方**: 确保末尾节点的next为None，避免形成循环
        bigger.next = None
        smaller.next = dummy_bigger.next
        return dummy_smaller.next

# @lc code=end

"""
1 4 3 2 5 2
x = 3

smaller -201 1 2 2
bigger 201 4 3 5
"""