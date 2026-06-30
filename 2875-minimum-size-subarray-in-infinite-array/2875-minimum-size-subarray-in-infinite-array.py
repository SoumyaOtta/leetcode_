class Solution:
    def minSizeSubarray(self, nums, target):
        n = len(nums)
        total = sum(nums)

        repeat = target // total
        rem = target % total

        if rem == 0:
            return repeat * n

        nums = nums + nums

        left = 0
        curr = 0
        ans = float("inf")

        for right in range(len(nums)):
            curr += nums[right]

            while curr > rem:
                curr -= nums[left]
                left += 1

            if curr == rem:
                ans = min(ans, right - left + 1)

        if ans == float("inf"):
            return -1

        return repeat * n + ans