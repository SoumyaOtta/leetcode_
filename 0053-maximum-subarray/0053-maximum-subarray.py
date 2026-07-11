class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            v = best + nums[i]
            u = nums[i]
            best = max(v, u)
            ans = max(ans, best)
        return ans
        