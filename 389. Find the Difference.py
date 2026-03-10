class Solution(object):
    def findTheDifference(self, s, t):
        my_dict = {}
        new_s = list(s)
        for i in new_s:
            if not i in my_dict:
                my_dict[i]=1
            else: my_dict[i]+=1
        for i in t:
            if i in my_dict:
                my_dict[i]-=1
                if my_dict[i] < 0:
                    return i
            else:
                return i
