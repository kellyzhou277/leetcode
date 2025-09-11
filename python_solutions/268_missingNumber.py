class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums_set = set(nums)
        for i in range(n + 1):
            if i not in nums_set:
                return i
        return False

def test_solution():
    solution = Solution()
    list1 = [0,1,3]
    print(f"Test 1: {solution.missingNumber(list1)}")
if __name__ == "__main__":
    test_solution()