#given an array, return the indices of two #s that add up to the target
#initialize a dict with indices and the num itself,
#iterate through the array, check if the diff between the num is in the dict
#return the indices of both nums
import unittest

class Solution:
    #brute force
    def twoSum_bruteForce(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
    #O(n) solution using hashmap
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dict:
                return [nums_dict[complement], i]
            nums_dict[nums[i]] = i
    

class unittest_solution(unittest.TestCase):
    def test_TwoSum(self):
        solution = Solution()
        result = solution.twoSum([2,7,11,15],9)
        self.assertEqual(result, [0,1])
        result2 = solution.twoSum_bruteForce([2,7,11,15],9)
        self.assertEqual(result2, [0,1])

def test_solution():
    solution = Solution()
    nums1 = [2,7,11,15]
    target1 = 9
    print(f"Test 1: {solution.twoSum(nums1, target1)}")

if __name__ == "__main__":
    test_solution()
    unittest.main()