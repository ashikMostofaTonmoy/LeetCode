from collections import Counter


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counted = Counter(nums).most_common()
        print(counted)
        print(f"counted[0][1] : {counted[0][1]}")
        if counted[0][1] > 1:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    x = s.containsDuplicate([1, 2, 3])
    print(x)
