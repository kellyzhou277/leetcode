#given an array, return the indices of two #s that add up to the target
#initialize a dict with indices and the num itself,
#iterate through the array, check if the diff between the num is in the dict
#return the indices of both nums

class Solution():
    def twoSum(self, nums, target):
        indices_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in indices_dict:
                return [indices_dict[diff], i]
            indices_dict[num] = i

def test_solution():
    solution = Solution()
    nums1 = [2,7,11,15]
    target1 = 9
    print(f"Test 1: {solution.twoSum(nums1, target1)}")

if __name__ == "__main__":
    test_solution()