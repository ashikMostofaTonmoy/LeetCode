class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n= len(nums)
        # print(type(nums))
        # temp=nums[:-k]
        # print(temp)
        # nums=nums[-k:]
        # print(nums)
        # nums.extend(temp)
        # nums=nums[-k:]+nums[:-k]
        # print(nums)
        # print(type(nums))

        for i in range(k):
            nums.insert(0, nums.pop())
        # for i in range(k % len(nums)):
        #     nums.insert(0, nums.pop())
        
        