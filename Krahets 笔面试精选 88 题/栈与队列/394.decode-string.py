#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (60.17%)
# Likes:    12949
# Dislikes: 634
# Total Accepted:    905.5K
# Total Submissions: 1.5M
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; there are no extra
# white spaces, square brackets are well-formed, etc. Furthermore, you may
# assume that the original data does not contain any digits and that digits are
# only for those repeat numbers, k. For example, there will not be input like
# 3a or 2[4].
# 
# The test cases are generated so that the length of the output will never
# exceed 10^5.
# 
# 
# Example 1:
# 
# 
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# 
# 
# Example 2:
# 
# 
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# 
# 
# Example 3:
# 
# 
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets
# '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
# 
# 
#

# @lc code=start
class Solution:
    # def decodeString(self, s: str) -> str:
    #     stack_num = []  # 用于存储数字，即将需要重复的次数
    #     stack_letter = [""]  # 用于存储当前构建的字母
    #     num = 0  # 当前数字

    #     for token in s:
    #         if token.isdigit():  # 处理数字字符
    #             num = num * 10 + int(token)  # 处理多位数字

    #         elif token.isalpha():  # 处理字母字符
    #             stack_letter[-1] += token

    #         elif token == "[":  # 遇到'['开始新的重复单元
    #             stack_letter.append("")  # 准备新的字符串构建
    #             stack_num.append(num)  # 存下当前num
    #             num = 0  # 重置num

    #         elif token == "]":  # 碰到']'表示结束一个重复单元
    #             letter_pop = stack_letter.pop()
    #             num_pop = stack_num.pop()
    #             # 将构建好的字符串和数字结合拼入上一层
    #             stack_letter[-1] += letter_pop * num_pop

    #     return stack_letter[0]

    def decodeString(self, s: str) -> str:
        stack_num = []
        stack_letter = [""]

        n = len(s)
        i = 0

        while i < n:
            if s[i].isdigit():
                start = i
                while i < n and s[i].isdigit():
                    i += 1
                    continue
                num = int(s[start:i])

            elif s[i].isalpha():
                start = i
                while i < n and s[i].isalpha():
                    i += 1
                    continue
                stack_letter[-1] += s[start:i]

            elif s[i] == "[":
                stack_num.append(num)
                stack_letter.append("")
                i += 1

            elif s[i] == "]":
                letter_pop = stack_letter.pop()
                num_pop = stack_num.pop()
                stack_letter[-1] += letter_pop * num_pop
                i += 1

        return stack_letter[0]


# @lc code=end


"""
3[a2[c]]
stack_num 3 2
stack_letter "" "a" "c"

stack_num 3
stack_letter "" "acc"

stack_num
stack_letter "accaccacc"

abc2[d]
stack_num
stack_letter "abc"

stack_num 2
stack_letter "abc" "d"

stack_num
stack_letter "abcdd"

2[a]bc
stack_num 2
stack_letter "" "a"

stack_num
stack_letter "aa"
"""