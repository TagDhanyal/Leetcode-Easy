class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in arr:
                return [arr[complement], i]
                # you can also do this to go forward in a array {print(numbs[i])}
            arr[num] = i
        return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
indices = solution.twoSum(nums, target)
print(indices)
"""
you can reverse this array like this

"""
arr = [1, 2, 6, 10]

# this is going backwards in a array
index = len(numbs)-1 
while index >=0:
    print(index)
    index -= 1
