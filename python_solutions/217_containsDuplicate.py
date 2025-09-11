class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen_set = set()
        for num in nums:
            if num in seen_set:
                return True
            seen_set.add(num)
        return False

def test_solution():
    solution = Solution()
    list1 = [1,2,3,4,1]
    print(f"Test 1: {solution.containsDuplicate(list1)}")
if __name__ == "__main__":
    test_solution()
