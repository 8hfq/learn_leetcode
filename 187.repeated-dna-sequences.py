#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (38.38%)
# Likes:    681
# Dislikes: 264
# Total Accepted:    157K
# Total Submissions: 408.7K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
# 
# Example:
# 
# 
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
# 
# 
#

# @lc code=start
import collections
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = collections.defaultdict(int)
        for i in range(len(s)):
            sequences[s[i:i+10]] +=1
        res = []
        for key,value in sequences.items():
            if value>1:
                res.append(key)
        return res

# @lc code=end

