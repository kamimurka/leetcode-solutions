class Solution(object):
    def intersection(self, nums1, nums2):
        nums1_set=set(nums1)
        nums2_set=set(nums2)
        lst=[]
        for i in nums1_set:
            if i in nums2_set:
                lst.append(i)
        return lst
