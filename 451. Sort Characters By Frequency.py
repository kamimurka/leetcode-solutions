class Solution(object):
    def frequencySort(self, s):
        my_dict={}
        for i in s:
            if i in my_dict:
                my_dict[i]+=1
            else: my_dict[i]=1
        res=sorted(my_dict, key=my_dict.get, reverse=True)
        final_res=''
        for i in res:
           final_res+=i*my_dict[i]
        return final_resA
