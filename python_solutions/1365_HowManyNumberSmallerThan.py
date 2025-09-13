class Solution():
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_set = sorted(nums)
        nums_dict = {}
        for i in range(len(sorted_set)):
            if sorted_set[i] not in nums_dict:
                nums_dict[sorted_set[i]] = i
        res = []
        for num in nums:
            res.append(nums_dict[num])
        return res
def test_solution():
    solution = Solution()

