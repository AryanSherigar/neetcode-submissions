class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        ans = 0

        for n in nSet:
            if (n - 1) not in nSet:
                leng = 1
                while(n + leng) in nSet:
                    leng += 1
                ans = max(leng, ans)
        
        return ans