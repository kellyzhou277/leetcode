class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen_set = set()
        for num in nums:
            if num in seen_set:
                return True
            seen_set.add(num)
        return False

def test_solution():
    list1 = [1,2,3,4,1]
    print("Test 1", Solution().containsDuplicate(list1))

