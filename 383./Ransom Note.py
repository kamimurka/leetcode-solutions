class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        my_dict={}
        for i in magazine:
            my_dict[i]=my_dict.get(i, 0)+1
        for i in ransomNote:
            if i in my_dict:
                my_dict[i]-=1
                if my_dict[i] < 0:
                    return False
            else: return False
        return True
