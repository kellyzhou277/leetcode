#return all triplets that add up to 0

class Solution():
    def threeSum(self, nums):
        res = []
        #first, we will sort the numbers ascending order
        nums.sort()
        for i in range(len(nums)):
            #we will iterate until 0, bc if more than that we will
            #require a negative #, which we already
            #passed through
            if nums[i] > 0:
                break
            #if the num is 0 or if it's not a repeated number, we will perform the two sum method on it
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res
    #method to check if the number has complements that add up to 0 in the array
    def twoSumII(self, nums, i, res):
        #two pointers to iterate through the array
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

def test_solution():
    solution = Solution()
    nums1 = [-1,0,1,2,-1,-4]
    print(f"Test 1: {solution.threeSum(nums1)}")

if __name__ == "__main__":
    test_solution()

