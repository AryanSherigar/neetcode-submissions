class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cSum = 0

        for num in nums:
            if cSum < 0:
                cSum = 0
            cSum += num
            ans = max(ans, cSum)

        return ans
        