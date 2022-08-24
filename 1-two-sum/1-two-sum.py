class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ind, val in enumerate(nums):
            remaining = target - nums[ind]
            if remaining in seen:
                return [ind, seen[remaining]]
            else:
                seen[val] = ind