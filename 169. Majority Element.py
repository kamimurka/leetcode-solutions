class Solution(object):
    def majorityElement(self, nums):
        half = len(nums)/2
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i]+=1
            else:
                my_dict[i]=1
            if my_dict[i]>half:
                return i
        return max(my_dict, key=my_dict.get)
