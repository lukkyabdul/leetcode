class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix



obj = Solution()

n = int(input("Enter number of strings: "))
strs = []

print("Enter the strings:")
for i in range(n):
    strs.append(input())

print("Longest Common Prefix:", obj.longestCommonPrefix(strs))
