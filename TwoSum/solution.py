class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in arr:
                return [arr[complement], i]
            arr[num] = i
        return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
indices = solution.twoSum(nums, target)
print(indices)