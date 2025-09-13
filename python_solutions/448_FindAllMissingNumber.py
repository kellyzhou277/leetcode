class Solution():
    def findMissingNumber(self, nums:list[int]) -> list[int]:
        nums_set = set(nums)
        missing_list = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                missing_list.append(i)
        return missing_list
def test_solution():
    solution = Solution()
    list1 = [4,3,2,7,8,2,3,1]
    list2 = [1,1]
    print(f"Test 1: {solution.findMissingNumber(list1)}")
    print(f"Test 2: {solution.findMissingNumber(list2)}")
if __name__ == "__main__":
    test_solution()
