class Solution:
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in d:
                return [d[need], i]

            d[nums[i]] = i


obj = Solution()


result = obj.twoSum([2, 7, 11, 15], 9)

t
print(result)
