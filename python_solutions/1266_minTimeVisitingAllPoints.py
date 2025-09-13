class Solution():
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 0
        dist = 0
        for i in range(1, len(points)):
            change_x = abs(points[i][0] - points[i-1][0])
            change_y = abs(points[i][1] - points[i-1][1])
            dist_travel = max(change_x, change_y)
            dist += dist_travel
        return dist
class test_solution():
    solution = Solution()
    list1 = [[1,1], [5,6], [7,2]]
    print(f"the min distance is {solution.minTimeToVisitAllPoints(list1)}")