class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dis=nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]>nums[i-1] or i ==0:
                left= i+1
                right=len(nums)-1
                while(left < right):
                    Sum= nums[i]+nums[left]+nums[right]
                    if abs(Sum-target)<= abs(dis-target): 
                        dis=Sum
                    if Sum<=target:
                        left+=1
                        while left < right and nums[left] == nums[left-1]:left+=1
                    else:
                        right-=1
                        while left < right and nums[right] == nums[right+1]:right -=1
        return dis
