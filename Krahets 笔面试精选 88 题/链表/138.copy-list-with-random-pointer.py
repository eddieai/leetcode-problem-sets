#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (58.29%)
# Likes:    14204
# Dislikes: 1524
# Total Accepted:    1.4M
# Total Submissions: 2.4M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# A linked list of length n is given such that each node contains an additional
# random pointer, which could point to any node in the list, or null.
# 
# Construct a deep copy of the list. The deep copy should consist of exactly n
# brand new nodes, where each new node has its value set to the value of its
# corresponding original node. Both the next and random pointer of the new
# nodes should point to new nodes in the copied list such that the pointers in
# the original list and copied list represent the same list state. None of the
# pointers in the new list should point to nodes in the original list.
# 
# For example, if there are two nodes X and Y in the original list, where
# X.random --> Y, then for the corresponding two nodes x and y in the copied
# list, x.random --> y.
# 
# Return the head of the copied linked list.
# 
# The linked list is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
# 
# 
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random
# pointer points to, or null if it does not point to any node.
# 
# 
# Your code will only be given the head of the original linked list.
# 
# 
# Example 1:
# 
# 
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# Example 2:
# 
# 
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random is null or is pointing to some node in the linked list.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     if not head:
    #         return head

    #     curr = head
    #     curr_cp = Node(head.val)
    #     origin_copy = {}
    #     while curr:
    #         origin_copy[curr] = curr_cp
    #         if curr.next:
    #             curr_cp.next = Node(curr.next.val)
    #         curr = curr.next
    #         curr_cp = curr_cp.next

    #     curr = head
    #     curr_cp = origin_copy[head]
    #     while curr:
    #         if curr.random:
    #             curr_cp.random = origin_copy[curr.random]
    #         curr = curr.next
    #         curr_cp = curr_cp.next

    #     return origin_copy[head]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        # 第一遍遍历：创建新节点，将其插入到每个原节点的旁边
        curr = head
        while curr:
            new_node = Node(curr.val, next=curr.next)  # 创建新节点并插入
            curr.next = new_node
            curr = new_node.next  # 跳到旧节点的next

        # 第二遍遍历：复制随机指针
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next  # 设置新节点的random
            curr = curr.next.next  # 跳到下一个旧节点

        # 第三遍遍历：分离两个链表
        curr = head
        dummy = Node(0)  # 虚拟头节点
        curr_cp = dummy  # 用于连接新节点
        while curr:
            curr_cp.next = curr.next  # 收集新节点
            curr.next = curr.next.next  # 恢复旧链表
            curr_cp = curr_cp.next  # 移动到下一个新节点
            curr = curr.next  # 移动到下一个旧节点

        return dummy.next  # 返回新复制链表的头

# @lc code=end

