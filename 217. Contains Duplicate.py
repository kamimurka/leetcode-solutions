class Solution(object):
    def containsDuplicate(self, nums):
        my_dict = {}
        for i in nums:
            if i == my_dict.get(i):
                return True
            else:
                my_dict[i]=i
        return False
