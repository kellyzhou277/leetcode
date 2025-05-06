#
class Solution():
    def longestCommonPrefix(self, strs):
        if (len(strs) == 0):
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0: len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix

def test_solution():
    solution = Solution()
    strs1 = ["flower","flow","flight"]
    print(f"Test: {solution.longestCommonPrefix(strs1)}")

if __name__ == "__main__":
    test_solution()
