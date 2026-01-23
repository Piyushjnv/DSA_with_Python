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
                # print('hello')
            num_map[num] = i
            # print(num_map[num])

           

        return []
    
solution = Solution()
result = solution.twoSum([3,3], 6)
print(result)  # Output: [0, 1]