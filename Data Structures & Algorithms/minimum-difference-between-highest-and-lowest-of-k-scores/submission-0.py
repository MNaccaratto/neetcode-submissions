class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()

        left = 0
        right = k - 1

        res = float('inf')

        while right < len(nums):

            diff = nums[right] - nums[left]

            if res > diff:
                res = diff
            
            right += 1
            left += 1

        return res