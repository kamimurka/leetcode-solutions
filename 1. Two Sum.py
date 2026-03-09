class Solution(object):
    def twoSum(self, nums, target):
        my_dict = {}
        for i, value in enumerate(nums): # here
            if target-value in my_dict:
                return [my_dict[target-value], i]
            else:
                my_dict[value]=i
