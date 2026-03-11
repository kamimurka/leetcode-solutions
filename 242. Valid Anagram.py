class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        my_dict = {}
        for item in s:
            if item not in my_dict:
                my_dict[item]=1
            else:
                my_dict[item]+=1
        for item in t:
            if item not in my_dict:
                return False
            my_dict[item]-=1
            if my_dict[item]<0:
                return False
        return True
