class Solution(object):
    def wordPattern(self, pattern, s):
        my_dict={}
        new_s=s.split()
        new_pattern=list(pattern)
        if len(new_pattern) != len(new_s): return False
        for i in range(len(new_pattern)):
            word = new_s[i]
            char = new_pattern[i]
            if char in my_dict: # char-ключ (а,б..) word - значение в ключе dog, cat..
                if word != my_dict[char]:
                    return False
            elif word in my_dict.values():
                return False
            else:
                my_dict[char]=word
        return True
