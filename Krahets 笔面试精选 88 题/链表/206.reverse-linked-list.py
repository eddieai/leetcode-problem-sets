#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (78.00%)
# Likes:    22072
# Dislikes: 473
# Total Accepted:    4.7M
# Total Submissions: 6M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: [2,1]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# 
# 
# 
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head or not head.next:
    #         return head

    #     prev = None
    #     curr = head
    #     nxt = curr.next

    #     while curr:
    #         nxt = curr.next
    #         curr.next = prev

    #         prev = curr
    #         curr = nxt

    #     return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归终止条件
        if not head or not head.next:
            return head

        # 先反转子链表：
        p = self.reverseList(head.next)

        # 再更新指针：
        # 当递归调用返回时，我们已经将从第二个节点开始的链表反转完成（如从 2 -> 3 -> … 反转成了 … -> 3 -> 2）。
        # 此时，当前递归层就可以将第一个节点（head）链接到这个已经反转的子链表上。
        # 具体地说，head.next.next = head 让 head.next（即原链表的下一个节点）指向当前节点 head，完成链表中一段的反转。
        head.next.next = head
        head.next = None  # 当前节点指向None
        return p  # 返回新的头节点


# @lc code=end


"""
prev = None
curr = 1
next = curr.next = 2
curr.next = prev = None

prev = curr = 1
curr = next = 2
next = curr.next = 3
curr.next = prev = 1

...

prev = curr = 4
curr = next = 5
next = curr.next = None  <-
curr.next = prev = 4
"""