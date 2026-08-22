class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return [num_map[complement],i]
            num_map[num] = i

           

        return []
    
solution = Solution()
result = solution.twoSum([2,23,11,7], 9)
print(result)  # Output: [0, 1]