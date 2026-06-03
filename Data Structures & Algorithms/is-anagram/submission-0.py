class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        CountS, CountT = {}, {}

        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i],1)
            CountT[t[i]] = 1 + CountT.get(t[i],1)
        
        return CountS == CountT

        