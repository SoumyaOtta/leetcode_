class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        keep = arr[0]
        delete = float('-inf')
        ans = arr[0]

        for i in range(1, len(arr)):
            prevkeep = keep
            keep = max(arr[i], keep+arr[i])
            delete = max(delete + arr[i], prevkeep)
            ans = max(ans, keep, delete)
        return ans