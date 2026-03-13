class Solution(object):
    def isHappy(self, n):
        n_set = set()
        while n != 1:
            n = str(n) # 1
            n = [int(x) for x in n] # 2
            total=0
            for i in n:
                total = total+i*i
            if total in n_set:
                return False
            else:
                n=total
            n_set.add(total)
        return True
