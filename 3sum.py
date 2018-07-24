class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        new_result=[]
        tmp_list=[]
        result_list=[]
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]>nums[i-1] or i ==0:
                left= i+1
                right=len(nums)-1
                while(left < right):
                    if -nums[i]==nums[left]+nums[right]:
                        tmp_list.append([nums[i],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left < right and nums[left] == nums[left-1]:left+=1
                        while left < right and nums[right] == nums[right+1]:right -=1
                    elif -nums[i]>nums[left]+nums[right]:
                        left+=1
                    else:
                        right-=1

        return tmp_list
