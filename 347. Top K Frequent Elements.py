class Solution(object):
    def topKFrequent(self, nums, k):
        my_dict={}
        res=[]
        for i in nums:
            if i in my_dict:
                my_dict[i]+=1
            else: my_dict[i]=1
        res = sorted(my_dict.items(), key=lambda x: x[1])
        final_res = res[-k:]
        return [x[0] for x in final_res]
