from collections import Counter


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counted = Counter(nums).most_common()
        return counted[-1][0]
