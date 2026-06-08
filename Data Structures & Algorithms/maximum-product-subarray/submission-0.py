class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = nums[0]
        cMin, cMax = 1, 1

        for num in nums:
            temp = cMax*num
            cMax = max(cMax*num, num * cMin, num)
            cMin = min(temp,num*cMin, num)
            ans = max(ans, cMax)

        return ans     