class Solution:
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in d:
                return [d[need], i]

            d[nums[i]] = i


# Create an object
obj = Solution()

# Call the function
result = obj.twoSum([2, 7, 11, 15], 9)

# Print the result
print(result)