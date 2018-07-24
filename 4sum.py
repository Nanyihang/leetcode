class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result_list=[]
        tmp_list=[]
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                left = j+1
                right = len(nums)-1
                while(left<right):
                    Sum=nums[i]+nums[j]+nums[left]+nums[right]
                    if Sum == target:
                        result_list.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]: left+=1
                        while left<right and nums[right]==nums[right+1]:right-=1  
                    elif Sum < target:
                        left += 1
                    else:
                        right -= 1
        for i in result_list:
            if i not in tmp_list:
                tmp_list.append(i)
        return tmp_list
