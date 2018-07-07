class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        for i in range(len(nums)):
            tmp= nums[i]
            if target-tmp in dict:
                return (dict[target-tmp],i)
            dict[tmp]=i
