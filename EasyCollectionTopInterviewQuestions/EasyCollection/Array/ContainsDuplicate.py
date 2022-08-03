from collections import Counter


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counted = Counter(nums).most_common()
        if counted[0][1] > 1:
            return True
        else:
            return False
